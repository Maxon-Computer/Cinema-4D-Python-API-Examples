"""Demonstrates the core concepts of graph descriptions by creating a simple material.

This script will create a red metallic material with an index of refraction of 1.1415 in the Redshift
node space. To run the script, paste it into the Script Manager of Cinema 4D and execute it.

Note:
    This is the narrative version of the hello_world script. See hello_world_brief.py for the brief
    version of this script.
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2024 Maxon Computer GmbH"
__version__ = "2025.0.0+"

import c4d
import maxon

doc: c4d.documents.BaseDocument # The active document

def main() -> None:
    """Called when Cinema 4D runs this script.
    """
    # Graph descriptions require a graph to which the description is applied. This graph can be
    # sourced with methods from the Nodes API or the convenience function GraphDescription.GetGraph().
    # GetGraph() can be used to both create new graphs (and implicitly with that a new material) or
    # to retrieve existing graphs from materials and other scene elements.

    # The following call creates a new graph which is attached to a new material named "Hello World".
    # We do manually specify for which node space we want to retrieve the graph. This information
    # could also be omitted, in which case Cinema 4D will return the graph for the active node space.
    # The active node space is effectively the currently selected render engine.
    graph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        name="Hello World", nodeSpaceId=maxon.NodeSpaceIdentifiers.RedshiftMaterial)

    # Now that we have our graph, we can start modifying it with a graph description. Note that graph
    # descriptions always build upon the existing content of a graph. Our graph does not contain any
    # content yet as we just created it, but if it would, our ApplyDescription() call would add to
    # that graph, and not overwrite it.

    # Graph descriptions are carried out with the method ApplyDescription(). The method must take at
    # least two arguments: the graph to which the description is applied and the description itself.
    maxon.GraphDescription.ApplyDescription(
        # The graph to which the description is applied.
        graph, 
        # The description itself. This is a dictionary that describes the structure of the graph.
        # We are describing here a very simple graph of the structure:
        #
        #       Standard Material > outColor <----------> Surface < Output
        #
        # I.e., a Standard Material node which is connected via its outColor output port to the 
        # Surface input port of an Output node. Note that while we read graphs usually from left to
        # right, from many nodes to a singular terminal node, in the case of Redshift the Output 
        # node, graph descriptions flip this on its head and describe the graph from the terminal
        # node to the many nodes.
        #
        # The nodes in graph description are describes as nested Python dictionaries (a pair of curly 
        # braces). In the jargon of graph descriptions, such dictionary is called a "scope".
        {
            # Because this is a set of curly braces, a scope, we are describing here a node. When we
            # want to describe a new node, this means we must name its type. This is done by using 
            # one of the special fields of graph descriptions. Special fields are denoted by a '$'
            # prefix. 

            # We declare that the new node we are describing here is an "Output" node. Graph 
            # descriptions have the ability to reference nodes, ports, and attributes by their 
            # interface label in addition to their API identifier. This works only for English 
            # language interface labels at the moment, but means that you can just type what you
            # see in the interface of Cinema 4D to describe a node, port, or attribute.
            "$type": "Output",

            # Now we are describing the input ports of the Output node and the values and connections
            # they have. We only want to connect the Surface input port of the Output node to the
            # outColor output port of the Standard Material node. To do this, we reference the
            # Surface input port of the Output node by its interface label and then open a new scope
            # to signal that we do not just want to set a literal but describe a connection.
            "Surface": {
                # Since we are inside a new scope here, this means we are describing a new node (
                # which is connected to the Surface input port of the Output node). So, the first
                # thing we do is again to declare the type of the node we are describing (note that
                # the order of attributes in a scope does not actually matter).

                # We declare that the new node we are describing here is a "Standard Material" node.
                "$type": "Standard Material",

                # Now we are going to set a few ports of the node, but other than in the previous
                # case we set these ports to literal values, i.e., constant values that are not
                # forwarded by a connection. Just as if we would have entered these values in 
                # Attribute Manger of a node.

                # Set the base color to pure red. Note that for vectors/colors we can also write:
                #
                #   "Base/Color": maxon.Vector(1, 0, 0)
                #   "Base/Color": maxon.Color(1, 0, 0)
                #   "Base/Color": c4d.Vector(1, 0, 0)
                #
                # Graph descriptions will automatically convert these values to the correct type and
                # also support the tuple notation we use here.
                "Base/Color": (1, 0, 0),

                # Set the metalness of the material to 1.0, i.e., a fully metallic material. Note 
                # that we wrote above "Base/Color" and here just "Metalness". The reason for this is
                # that label references must be unambiguous. Because there is also a "Reflection/Color"
                # port and many other ports named "Color" in the Standard Material node, we must make
                # that port reference unambiguous by prefixing it with the attribute group it belongs 
                # to. The absolute label references bot ports would be
                #
                #   "Base Properties/Base/Color"
                #   "Base Properties/Base/Metalness"
                #
                # But since there are not two ports named "Color" in a attribute group called "Base",
                # we can just write "Base/Color" for our color port and just "Metalness" for our
                # metalness port, since its port name is unique in the node.
                "Metalness": 1.0,

                # The index of refraction of the material. 
                "Reflection/IOR": 1.1415
            } # The end of the Standard Material node scope.
        } # The end of the Output node scope.
    ) # The end of the ApplyDescription() call.

if __name__ == "__main__":
    main()