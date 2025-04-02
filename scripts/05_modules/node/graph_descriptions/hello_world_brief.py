"""Demonstrates the core concepts of graph descriptions by creating a simple material.

This script will create a red metallic material with an index of refraction of 1.1415 in the Redshift
node space. To run the script, paste it into the Script Manager of Cinema 4D and execute it.

Note:
    This is the brief version of the hello_world script. See hello_world_narrative.py for a narrative
    documentation of this script.
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
    # Get a new  material named "Hello World" which has a graph in the Redshift node space.
    graph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        name="Hello World", nodeSpaceId=maxon.NodeSpaceIdentifiers.RedshiftMaterial)

    # Apply a graph description to the graph.
    maxon.GraphDescription.ApplyDescription(
        graph, 
        # The description which is applied to the graph. We are going to write a simple description
        # of a Standard Material node connected to an Output node. Note that graph descriptions flip
        # the reading direction of graphs from the usual left-to-right to right-to-left. They
        # start out with the terminal end node of the graph and then describe the nodes leading to
        # that node. Each scope (a pair of curly braces) in the description describes a node.
        {
            # We describe the terminal Output node of the graph.
            "$type": "Output",

            # We describe the value of the Surface port of the Output node which is connected to the
            # outColor port of a Standard Material node.
            "Surface": {
                "$type": "Standard Material",

                # We set a  few ports of the Standard Material node to literals, i.e., constant 
                # values that are not driven by other nodes.
                "Base/Color": (1, 0, 0),
                "Metalness": 1.0,
                "Reflection/IOR": 1.1415
            } 
        }
    )

if __name__ == "__main__":
    main()