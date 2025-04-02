"""Demonstrates how to retrieve graphs from scene elements.

To run the script, paste it into the Script Manager of Cinema 4D and execute it.
"""
import c4d
import maxon
import mxutils

__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2024 Maxon Computer GmbH"
__version__ = "2025.0.0+"

doc: c4d.documents.BaseDocument # The active document

def main() -> None:
    """Called when Cinema 4D runs this script.
    """
    # The most common use case for GetGraph is to create a new material and graph from scratch.
    # The call below will result in a new material being created in the active document with the
    # name "matA". Since we are not passing an explicit node space, the currently active material
    # node space will be used (which usually is the Redshift node space for most users).
    graphA: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(name="ActiveNodeSpace")
    print(f"{graphA = }")

    # This will create a material named "matB" that has a graph in the Redshift material node space,
    # no matter what the currently active material node space is.
    graphB: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        name="RedshiftSpace", nodeSpaceId=maxon.NodeSpaceIdentifiers.RedshiftMaterial)
    print(f"{graphB = }")

    # But we can also use the function to create or get a graph from an existing material. The call
    # below will either create a new Redshift graph for the first material in the document #material
    # or return its existing Redshift graph. The CheckType call exists so that the script halts when 
    # there is no materials in a document. But since we just crated #matA and #matB, we will here 
    # just retrieve the graph from "matB" (because new materials inserted in front at not at the end). 
    # I.e., #graphB and #graphC are the same.
    material: c4d.BaseMaterial = mxutils.CheckType(doc.GetFirstMaterial())
    graphC: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        material, nodeSpaceId=maxon.NodeSpaceIdentifiers.RedshiftMaterial)
    print(f"{graphC = }")
    print(f"{graphB == graphC = }")

    # We could also create a Standard Renderer graph, or a third party render engine graph such
    # as Arnold or VRay for example.
    graphStandard: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        name="StandardSpace", nodeSpaceId=maxon.NodeSpaceIdentifiers.StandardMaterial)
    
    try:
        vrayGraph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
            name="VRaySpace", nodeSpaceId="com.chaos.class.vray_node_renderer_nodespace")
    except Exception as e:
        print (e)

    # We can also pass a document or an object for the first argument #element of GetGraph. If we
    # pass a document, it will yield the scene nodes graph of that document, and if we pass an object,
    # it will yield its capsule graph (if it has one).
    sceneGraph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(doc)
    print(f"{sceneGraph = }") 

    # Finally, we can determine the contents of a newly created graph. We can either get an empty
    # graph or the so-called default graph with a few default nodes as it would be created in
    # Cinema 4D when the user creates a new graph for that space. #createEmpty=True is the default
    # of a #GetGraph call.
    emptyGraph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        name="ActiveSpaceEmptyGraph", createEmpty=True)
    defaultGraph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        name="ActiveSpaceDefaultGraph", createEmpty=False)
    
    # Finally, there is also GraphDescription.GetMaterialGraphs which simplifies iterating over all
    # material graphs of a given node space in a document. This can simplify carrying out batch
    # operations on material graphs for a specific render engine, while keeping other render engines
    # untouched. Other than GetGraph, this function will not create new graphs when none exist.

     # Print all Redshift renderer material graphs in a document. This will be at least one graph,
     # because created explicitly one in this script.
    graph: maxon.NodesGraphModelRef
    for graph in maxon.GraphDescription.GetMaterialGraphs(doc, maxon.NodeSpaceIdentifiers.RedshiftMaterial):
        print(f"Redshift graph: {graph}")

    # Same for the Standard renderer material graphs. This will also be at least one graph, because
    # created explicitly one in this script.
    for graph in maxon.GraphDescription.GetMaterialGraphs(doc, maxon.NodeSpaceIdentifiers.StandardMaterial):
        print(f"Standard graph: {graph}")

if __name__ == "__main__":
    main()