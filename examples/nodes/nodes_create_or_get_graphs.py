#coding: utf-8
"""Demonstrates creating or getting node graphs in a scene.

Topics:
    * Getting or creating a graph for a material
    * Getting or creating a graph for a scene element (scene nodes, capsule, etc.)
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__date__ = "06/08/2026"
__license__ = "Apache-2.0 License"
__version__ = "2027.0.0"

import c4d
import maxon
import mxutils

doc: c4d.documents.BaseDocument # The active document.

mxutils.REPORT()
def GraphDescriptionGetGraphExample() -> None:
    """Demonstrates creating or getting node graphs in a scene using the convenience function 
    `maxon.GraphDescription.GetGraph`.
    """
    # The most common use case for GetGraph is to create a new material and graph from scratch. 
    # The call below will result in a new material being created in the active document with the
    # name "matA". Since we are not passing an explicit node space, the currently active material
    # node space will be used. We could also pass c4d.GetActiveNodeSpaceId() to the same effect.
    graphA: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(name="matA")
    print (f"Created new material with graph: {graphA}")

    # This will create a material named "matB" that has a graph in the Redshift material node space, 
    # no matter what the currently active material node space is.
    graphB: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        name="matB", nodeSpaceId=maxon.NodeSpaceIdentifiers.RedshiftMaterial)
    print (f"Created new Redshift material with graph: {graphB}")

    # We could also use a literal for the node space ID instead of the constant above. For third
    # party node spaces, you must ask the vendor for the node space ID to use.
    graphC: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        name="matC", nodeSpaceId="com.redshift3d.redshift4c4d.class.nodespace")
    print (f"Created new Redshift material with graph: {graphC}")

    # But we can also use the function to create or get a graph from an existing material. We get
    # the first material in the document and either get its existing graph in the Redshift material 
    # node space or create a new one if it does not exist yet.
    material: c4d.BaseMaterial = mxutils.CheckType(doc.GetFirstMaterial())
    graphD: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        material, nodeSpaceId=maxon.NodeSpaceIdentifiers.RedshiftMaterial)
    print (f"Got or created Redshift graph for material {material.GetName()}: {graphD}")

    # We can also pass a document or an object for the first argument #element of GetGraph. If we 
    # pass a document, it will yield the scene nodes graph of that document, and if we pass an object,
    # it will yield its capsule graph (if it has one).
    sceneGraph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(doc)
    print (f"Got scene graph for document: {sceneGraph}")
    # capsuleGraph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(doc.GetFirstObject())

    # Finally, we can determine the contents of a newly created graph. We can either get an empty 
    # graph or the so-called default graph with a few default nodes as it would be created in 
    # Cinema 4D when the user creates a new graph for that space.
    emptyGraph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        name="emptyMat", createEmpty=True) # The default
    defaultGraph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        name="defaultMat", createEmpty=False)
    print (f"Created empty graph: {emptyGraph}")
    print (f"Created default graph: {defaultGraph}")


mxutils.REPORT()
def ManualGetGraphExample() -> None:
    """Demonstrates creating or getting graphs in a scene by manually interacting with the Cinema API 
    and Maxon API. This is a more verbose way of doing the same thing as `GraphDescriptionGetGraphExample`.
    """
    # --- Materials --------------------------------------------------------------------------------

    # Create a new material and add it to the document.
    material: c4d.BaseMaterial = mxutils.CheckType(c4d.BaseMaterial(c4d.Mmaterial))
    material.SetName("mat_manual")
    doc.InsertMaterial(material)

    # Get the node material for it and add a graph for the currently active material space to it.
    nodeMaterial: c4d.NodeMaterial = material.GetNodeMaterialReference()
    graph: maxon.GraphModelInterface = nodeMaterial.CreateDefaultGraph(c4d.GetActiveNodeSpaceId())
    if graph.IsNullValue():
        raise RuntimeError("Could not add graph to material.")
    
    # The method #CreateDefaultGraph we used above does not create an empty graph, but the setup
    # the respective node space considers to be its default setup. For Redshift this is for example
    # an RS Standard Material node connected to an Output end node.
    print (f"Nodes in CreateDefaultGraph setup for material {material.GetName()}:")
    for node in graph.GetViewRoot().GetInnerNodes(mask=maxon.NODE_KIND.NODE, includeThis=False):
        print (f"{node}")

    # Remove the graph we just created.
    nodeMaterial.RemoveGraph(c4d.GetActiveNodeSpaceId())

    # We can also create an empty graph which contains no nodes at all with. 
    graph: maxon.GraphModelInterface = nodeMaterial.CreateEmptyGraph(c4d.GetActiveNodeSpaceId())
    if graph.IsNullValue():
        raise RuntimeError("Could not add graph to material.")

    print (f"Nodes in CreateEmptyGraph setup for material {material.GetName()}:")
    for node in graph.GetViewRoot().GetInnerNodes(mask=maxon.NODE_KIND.NODE, includeThis=False):
        print (f"{node}")

    # Remove the graph again.
    nodeMaterial.RemoveGraph(c4d.GetActiveNodeSpaceId())

    # Finally, we should be aware that node material can hold graphs for multiple node spaces and
    # therefore can be used with multiple render engines. To do this, we can simply add multiple
    # graphs for specific nodes spaces.

    # Add a default graph for both the Redshift and Standard material node space, check the "Basic"
    # tab of the material, it will list a graph for both spaces. When you switch between render 
    # engines, the material will have its own graph for each engine. To support 3rd party render
    # engines, you must ask their vendor for their node space ID.
    nodeMaterial.CreateDefaultGraph(maxon.NodeSpaceIdentifiers.RedshiftMaterial)
    nodeMaterial.CreateDefaultGraph(maxon.NodeSpaceIdentifiers.StandardMaterial)

    # --- Scene Nodes ------------------------------------------------------------------------------

    # All Nodes API graphs are attached to a Cinema API scene element via a `NimbusBaseRef`. We could 
    # technically do the same for materials, but there the NodeMaterial type simplifies things a bit
    # for us. For scene nodes, be it the global scene graph or a capsule graph, we have to get the 
    # `NimbusRef` for the scene element first. The global graph is attached to the scene hook, which 
    # is a special scene element that is always present in the scene (the word 'scene' in Scene Hooks
    # does not refer to Scene Nodes, it is a coincidence that they both use the word 'scene').

    # Get the scene hook for the global Neutron graph (Neutron is the internal name for Scene Nodes).
    nodeHost: c4d.BaseList2D = mxutils.CheckType(doc.FindSceneHook(maxon.neutron.SCENEHOOK_ID))

    # Make sure the global neutron graph exists. This is only something we to for the global neutron
    # graph, for capsules and materials this step can be omitted.
    if not nodeHost.Message(maxon.neutron.MSG_CREATE_IF_REQUIRED):
        raise RuntimeError("Could not create scene graph.")

    # Check if the scene element #nodeHost actually holds nodes and then get its scene nodes graph.
    if not nodeHost.IsNodeBased():
        raise RuntimeError("This scene element does not hold nodes.")
    
    handle: maxon.NimbusBaseRef | None = nodeHost.GetNimbusRef(maxon.NodeSpaceIdentifiers.SceneNodes)
    if handle is None:
        raise RuntimeError("Could not get NimbusBaseRef for scene nodes.")

    graph: maxon.GraphModelRef = handle.GetGraph()
    print (f"Got scene graph for document: {graph}")

    # See also _associate_nodes.py for an example of how to iterate over the nodes in a graph and 
    # find their corresponding Cinema API surrogate nodes, which is one of the major purposes of
    # the type #NimbusBaseRef.
    

def main():
    """Runs the example.
    """
    # Run the example that demonstrates creating or getting graphs in a scene using the convenience 
    # function `maxon.GraphDescription.GetGraph`.
    GraphDescriptionGetGraphExample()

    # Run the example that demonstrates creating or getting graphs in a scene manually.
    ManualGetGraphExample()


if __name__ == "__main__":
    main()
