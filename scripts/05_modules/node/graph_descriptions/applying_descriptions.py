"""Demonstrates the technical aspects of #GraphDescription.ApplyDescription calls.

To run the script, paste it into the Script Manager of Cinema 4D and execute it.

Note:
    This example is more about the technical aspects of #GraphDescription.ApplyDescription and
    therefore less relevant for beginners.
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
    # The graph description we are going to apply in the different #ApplyDescription calls, the
    # content of the graph is here irrelevant for this example, other than it is intended for a
    # Redshift material graph.
    redshiftDescription: dict = {
        "$type": "Output",
        "Surface": {
            "$type": "Standard Material",
            "Base/Color": (1, 0, 0),
            "Metalness": 1.0,
            "Reflection/IOR": 1.1415
        } 
    }

    # A Standard Renderer and Redshift material graph we are going to use in the example.
    standardGraph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        name="Standard Material", nodeSpaceId=maxon.NodeSpaceIdentifiers.StandardMaterial)
    redshiftGraph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        name="Redshift Material", nodeSpaceId=maxon.NodeSpaceIdentifiers.RedshiftMaterial)

    # This is how we usually call #ApplyDescription, we just pass the graph to modify and the
    # description to apply.
    maxon.GraphDescription.ApplyDescription(redshiftGraph, redshiftDescription)

    # A description that is not intended for the graph its is applied to will always fail at some
    # point because the node types referenced in the description are then not contained in the node
    # space of the graph. But because node spaces share some node types, as for example the value
    # node, it can take some time until the graph description fails. But one can never end up with
    # a half way executed graph description due to the transaction logic of the Nodes API. A graph
    # description #ApplyDescription call either succeeds in its entirety or fails as a whole.
    
    # This cannot work, we are trying to apply a Redshift graph description to a standard graph.
    try: 
        maxon.GraphDescription.ApplyDescription(standardGraph, redshiftDescription)
    except Exception as e:
        print(e) # Will print :
        # "The node type reference 'Output' (lang: 'en-US', space: 'net.maxon.nodespace.standard') 
        #   is not associated with any IDs. [graphdescription_impl.cpp(1648)] ..."

    # #ApplyDescription offers a node space ID argument which allows the user to manually state of
    # which type the passed graph description is. There is no concrete technical advantage in doing
    # this other than ending up with more verbose code and the fact that such calls for a mis-matching
    # graph will fail right away and not only when already half of the description has been executed
    # and the graph then having to be unwound for a failed graph transaction.

    # Cannot work either, but might will a bit more gracefully for complex graph descriptions.
    try: 
        maxon.GraphDescription.ApplyDescription(
            standardGraph, redshiftDescription, nodeSpace=maxon.NodeSpaceIdentifiers.RedshiftMaterial)
    except Exception as e:
        print(e) # Will print:
        # "User defined node space 'com.redshift3d.redshift4c4d.class.nodespace' does not match 
        #   passed graph."

    # A more impactful option is the language of the graph description. Currently graph descriptions
    # only support the English language for label references. When no language is given, Cinema 4D
    # assumes the system language (because at its core graph descriptions are already designed for
    # other languages environments than en the English language). By passing "en-US" we can force
    # force a non-English interface labels Cinema 4D instance to resolve the graph description as if
    # it were English.

    maxon.GraphDescription.ApplyDescription(
            standardGraph, redshiftDescription, nodeSpace=maxon.NodeSpaceIdentifiers.RedshiftMaterial)
    
if __name__ == "__main__":
    main()