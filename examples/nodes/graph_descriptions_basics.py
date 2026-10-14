"""Demonstrates how graph descriptions create and modify node graphs.

Builds material graphs from nested scopes, sets literal port values, reuses nodes by identifier,
and makes implicit or explicit connections. It also contrasts a list of partial descriptions with
successive GraphDescription.ApplyDescription calls on the same graph.

Note:
    This example is written for the Redshift Material nodes, it will only work when you have
    Redshift installed. But the same principles will also work in any other node space, such as
    Standard Render, Vray, Arnold, etc.
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2025 MAXON Computer GmbH"
__date__ = "29/07/2026"
__license__ = "Apache-2.0 License"
__version__ = "2027.0.0"

import math

import c4d
import maxon
import mxutils

doc: c4d.documents.BaseDocument  # The active document.


# This os an intentionally uncommented example for graph descriptions uses in the docs to showcase
# the look and syntax of graph descriptions in an unobstructed manner.
def SimpleGraphDescription() -> None:
    """Creates a red metallic OpenPBR Material.
    """
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Hello World"), {
            maxon.GraphDescription.Type: "Output",
            "Surface": {
                maxon.GraphDescription.Type: "OpenPBR Material",
                "Base/Color": (1, 0, 0),
                "Base/Metalness": 1.0,
                "Specular/IOR": 2 * math.pi
            }
        }
    )


# Same example as above, but with comments explaining the syntax and logic of graph descriptions.
def CommentedSimpleGraphDescription() -> None:
    """Explains how nested scopes express node creation and port connections.
    """
    # A GraphDescription.ApplyDescription call must take at least two arguments:
    maxon.GraphDescription.ApplyDescription(

        # 1. A graph to write the description to, in this case we use GetGraph to create a new node
        # material and get its graph for the currently active material node space; Redshift by default.

        maxon.GraphDescription.GetGraph(name="Hello World"),

        # 2. And the graph descriptions to write into that graph. They follow an inverted, right-to-left
        # reading pattern compared to the Node Editor (where we tend to read left-to-right). Each 
        # node in the graph has its own scope (a pair of curly braces). Connections between nodes in 
        # the graph are described by nesting scopes.
        {
            # This outmost scope is of type "Output". It tells Cinema 4D that we want to create an
            # Output node. Instead of GraphDescription.Type, we could also write "$type".
            maxon.GraphDescription.Type: "Output",

            # We reference its 'Surface' input port to either set a value or connect it to another
            # node. In this case we create a new node, indicated by opening a new scope (the set of
            # curly braces). Because most (material) nodes only have one output port, we do not have
            # to specify here that we want to connect to the 'outColor' port of the 'OpenPBR Material'
            # node we are going to create, the output port is implicit.
            "Surface": {
                # Just as before, we declare the type of node this scope describes.
                maxon.GraphDescription.Type: "OpenPBR Material",

                "Base/Color": (1, 0, 0),
                "Base/Metalness": 1.0,
                "Specular/IOR": 2 * math.pi
            }
        }
    )


def GettingGraphs(doc: object) -> None:
    """Obtains new and existing material, scene, and capsule graphs with GraphDescription.GetGraph.
    """
    # The most common use case for GetGraph is to create a new material and graph from scratch.
    # The call below will result in a new material being created in the active document with the
    # name "matA". Since we are not passing an explicit node space, the currently active material
    # node space will be used.
    graphA: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(name="mat_implicit_nodespace(empty)")

    # This will create a material named "matB" that has a graph in the Redshift material node space,
    # no matter what the currently active material node space is.
    graphB: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        name="mat_explicit_nodespeace", nodeSpaceId=maxon.NodeSpaceIdentifiers.RedshiftMaterial)

    # But we can also use the function to create or get a graph from an existing material. The call
    # below will either create a new Redshift graph for #material or return the existing one.
    material: c4d.BaseMaterial = mxutils.CheckType(doc.GetFirstMaterial())
    graphC: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        material, nodeSpaceId=maxon.NodeSpaceIdentifiers.RedshiftMaterial)

    # We can also pass a document or an object for the first argument #element of GetGraph. If we
    # pass a document, it will yield the scene nodes graph of that document, and if we pass an object,
    # it will yield its capsule graph (if it has one).
    sceneGraph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(doc)
    # capsuleGraph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(doc.GetFirstObject())

    # Finally, we can determine the contents of a newly created graph. We can either get an empty
    # graph or the so-called default graph with a few default nodes as it would be created in
    # Cinema 4D when the user creates a new graph for that space.
    emptyGraph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(name="emptyMat", createEmpty=True)
    defaultGraph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(name="defaultMat", createEmpty=False)


def ScopesAndReferencedNodes() -> None:
    """Builds a material graph that shares one Value node through its graph description identifier.
    """
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Scopes and Values Example"), {
            "$type": "Output",
            # The surface input port of the output node does not have a literal value but describes
            # its value with a nested scope (the {}).
            "Surface -> outColor": {
                # Directly described is an OpenPBR Material node.
                "$type": "OpenPBR Material",
                # The metalness port is set as a literal value, here we do not open a new scope.
                "Base/Metalness": 1.,
                # But the base color is not a literal but connected to a texture node, we open a new scope.
                "Base/Color": {
                    "$type": "Texture",
                    # We set a literal value to the port-bundle child port Path by referencing an asset
                    # by its asset URL. If we wanted to reference a file on disk, we would use the "file"
                    # scheme, e.g., "file:///C:/path/to/file.png".
                    "Image/Filename/Path": "asset:///file_eb62aff065c50a2b",
                    # The scale of the texture is again not a literal but connected to a value node.
                    "Scale": {
                        "$type": "Value",
                        # Here we do something new, we set the id of this node in the graph so that we
                        # can later reference it as #texTransform.
                        "$id": "texTransform",
                        "#~in": (2, 2, 1)
                    }
                },
                # The specular roughness of the OpenPBR Material node, we use another texture here.
                "Specular/Roughness": {
                    "$type": "Texture",
                    "Image/Filename/Path": "asset:///file_8bf49bb0b9992dbe",
                    # Here is something new again, we neither set a literal value nor do we define
                    # a new node/scope to set the value of this Scale port. We reference the node with
                    # the id #texTransform as the value of the scale port. This will result in both
                    # ports being connected to the same value node.
                    "Scale": "#texTransform"
                },
                # The Bump Map port of the OpenPBR Material node, we connect a Bump Map node
                # connected to a texture node reusing our #texTransform value node again.
                "Geometry/Bump Map": {
                    "$type": "Bump Map",
                    "Input Map Type": 0,
                    "Height Scale": .2,
                    "Input": {
                        "$type": "Texture",
                        "Image/Filename/Path": "asset:///file_e706df60a3a533d2",
                        "Scale": "#texTransform"
                    }
                }
            }
        })


def LazyLiterals() -> None:
    """Builds a material graph that uses lazy values for the color and texture paths.
    """
    # Literals are attribute and port values that you directly type out in description (instead of 
    # defining them with a connection). Lazy literals allow you to be less verbose when writing 
    # descriptions and let the Graph Description API handle the details at runtime.
    #
    # Since lazy literals are the defacto standard in graph description examples, this example does 
    # not show you something new, but rather shows you how such values formally would have to be set.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Lazy Literals Example"), {
            "$type": "Output",
            "Surface": {
                "$type": "OpenPBR Material",
                "Base/Metalness": 1.,
                "Base/Color": {
                    "$type": "Texture",
                    # The "Image/Filename/Path" port of this node type is of type maxon.Url. Normally, 
                    # we would have to create a maxon.Url object and pass it as the value of this port.
                    #
                    # Using lazy literals, we can just pass a string and the graph description system 
                    # will convert it to a maxon.Url object at runtime. The same will work for ports 
                    # and attributes of type maxon.Id, maxon.InternedId, and maxon.Uuid. Another lazy
                    # literal aspect is us using the user facing (fake) asset URL scheme "assetdb" 
                    # instead of the real asset URL scheme "asset".
                    "Image/Filename/Path": "assetdb:///Textures/Surfaces/Redshift/Metal/mxn_metal_aluminium_foil_crumbled-001_4k_roughness.jpg",

                    # The formal way to set this port, we wrap our url string in a maxon.Url object
                    # and use the "asset" URL scheme to reference an asset.
                    # "Image/Filename/Path": maxon.Url("asset:///file_eb62aff065c50a2b"),

                    # Another form of lazy literals can be vectors. The "General/UV/Remap/Scale" port
                    # uses a data type that is not wrapped for Python: maxon::Vector2d64. But we
                    # can just pass a tuple of two floats now, and the graph description system will 
                    # convert it to a maxon.Vector2d64 object at runtime. You can express any 2, 3, 
                    # or 4 component color or vector as a tuple.
                    "UV/Remap/Scale": (0.5, 0.5),
                },
                # The most important form of lazy literals are colors. They also support the
                # tuple form, but are also interpreted as sRGB values in OCIO documents now, i.e., 
                # the form users are used to from the UI.

                # Will write (1, 0, 0) as an sRGB value, i.e., very roughly (0.61, 0.07, 0.02) in 
                # ACEScg, the default render space of Cinema 4D.
                "Specular/Color": (1, 0, 0),

                # The formal way to set the specular color. We use explicit types, raw colors, and a
                # color converter to convert the color exactly from the input space we chose to
                # render space. See examples/rendering/ocio.py for details on converters. For this
                # wor work, we would have to set:
                #
                #   "$flags": maxon.GraphDescription.Flags.RAW_COLORS,
                #
                # In the top level scope of this description, so that the graph description system 
                # does not convert the color to render space on its own.
                # "Specular/Color": converter.TransformColor(
                #     maxon.Color(1, 0, 0), c4d.COLORSPACETRANSFORMATION_OCIO_SRGB_TO_RENDERING)
            }
        })


def ExplicitConnections() -> None:
    """Connects a named OpenPBR Material output explicitly to the Output Surface input.

    This mechanism is only needed when a node has multiple output ports and we want to connect a 
    specific one. In this case, the OpenPBR Material node has only one output port, so we could 
    have used the implicit connection mechanism as in the previous examples.
    """
    # The standard "Hello World" graph descriptions shown in many examples before.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Hello World (Explicit Connections)"), {
            "$type": "Output",
            # We describe the only connection in the graph explicitly. We connect the
            # OpenPBRMaterial.outColor port to the Output.Surface port. Or to express it in the 
            # graph description logic: The Output node has an input port named Surface, which 
            # connects to the outColor output port of the OpenPBR Material node we are going to 
            # create in this scope.
            "Surface -> outColor": {
                "$type": "OpenPBR Material",
                "Base/Color": (1, 0, 0),
                "Base/Metalness": 1.0,
            }
        }
    )


def PartialDescriptions() -> None:
    """Builds the same Color Mix graph from a partial-description list and successive applications.
    """
    maxon.GraphDescription.ApplyDescription(
        # Graph descriptions can actually consist of a list of partial descriptions applied to a graph.
        # Prior examples have always used the simplified single description form, but internally,
        # descriptions are always a list of partial descriptions. This also demonstrates that a
        # graph description does not have to necessarily describe a complete graph and can build
        # on existing nodes in a graph.
        maxon.GraphDescription.GetGraph(name="Partial Descriptions"), [
            # First we have three partial descriptions that add the Color nodes for red, green and 
            # blue to the graph.
            {
                "$type": "Color",
                "$id": "red",
                "Inputs/Color": (1, 0, 0, 1)
            },
            {
                "$type": "Color",
                "$id": "green",
                "Inputs/Color": (0, 1, 0, 1)
            },
            {
                "$type": "Color",
                "$id": "blue",
                "Inputs/Color": (0, 0, 1, 1)
            },
            # If we would end our description here, we would just have added three Color nodes to 
            # the graph. But we add a fourth partial description to add the two Color Mix nodes and 
            # wires up all five nodes.
            {
                "$type": "Color Mix",
                "Mix Amount": 0.5,
                "Input 1": "#red",
                "Input 2": {
                    "$type": "Color Mix",
                    "Mix Amount": 0.5,
                    "Input 1": "#green",
                    "Input 2": "#blue",
                },
            }]
    )

    # The former example could also be written as four #ApplyDescription calls and will result in exactly
    # the same graph. This shows also what might have been obfuscated a bit by earlier simpler examples:
    # #ApplyDescription indeed applies a description to a graph and can very well build on existing
    # content in a graph. This is an important fact for understanding what graph queries do.
    graph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(name="Singular Descriptions")

    # Add the three Color nodes in their own #ApplyDescription call each.
    maxon.GraphDescription.ApplyDescription(
        graph, {
            "$type": "Color",
            "$id": "red",
            "Inputs/Color": (1, 0, 0, 1)
        }
    )

    maxon.GraphDescription.ApplyDescription(
        graph, {
            "$type": "Color",
            "$id": "green",
            "Inputs/Color": (0, 1, 0, 1)
        }
    )

    maxon.GraphDescription.ApplyDescription(
        graph, {
            "$type": "Color",
            "$id": "blue",
            "Inputs/Color": (0, 0, 1, 1)
        }
    )

    # And finally wire everything together in a final call. We could also have done the same with a
    # material graph loaded from disk which contained these three disjunct color Nodes.
    maxon.GraphDescription.ApplyDescription(
        graph, {
            "$type": "Color Mix",
            "Mix Amount": 0.5,
            "Input 1": "#red",
            "Input 2": {
                "$type": "Color Mix",
                "Mix Amount": 0.5,
                "Input 1": "#green",
                "Input 2": "#blue",
            },
        }
    )


def GroupingNodes() -> None:
    """Demonstrates how to group nodes in a graph description.
    """
    # Grouping nodes follows a special syntax. Grouping is not embedded into an ongoing graph, as you 
    # otherwise run into issues when you want to group nodes in multiple parts of the graph, or group
    # nodes in an existing graph. But grouping nodes is also not a description command (see
    # graph_descriptions_commands.py), but a special form of top level scope.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Nested Texture Groups"), [
            # We create a new graph from scratch, and add IDs to the three texture nodes we create.
            {
                "$type": "Output",
                "Surface -> outColor": {
                    "$type": "OpenPBR Material",
                    "Base/Color": {
                        "$type": "Texture",
                        "$id": "albedo_texture",
                        "Image/Filename/Path": "asset:///file_eb62aff065c50a2b",
                    },
                    "Specular/Roughness": {
                        "$type": "Texture",
                        "$id": "roughness_texture",
                        "Image/Filename/Path": "asset:///file_8bf49bb0b9992dbe",
                    },
                    "Geometry/Bump Map": {
                        "$type": "Bump Map",
                        "Input": {
                            "$type": "Texture",
                            "$id": "height_texture",
                            "Image/Filename/Path": "asset:///file_e706df60a3a533d2",
                        },
                    },
                },
            },
            # In the next partial description, we use the special "$type": "Group" scope to group 
            # the two textures via their IDs that feed the Base Color and Specular Roughness ports 
            # of the OpenPBR Material node. A "$type": "Group" scope can only appear at the top 
            # level of a description. We can set its ID and special children field to a list of node
            # IDs that we want to group together. We can also set any attribute on that node, for
            # example its name. But any attempts to write a full description by addressing the ports 
            # of the group node will result in an error, as the only purpose of a group scope is to 
            # group nodes together.
            {
                "$type": "Group",
                "$id": "surface_textures",
                "$children": ["#albedo_texture", "#roughness_texture"],
                "Basic/Name": "Surface Textures",
            },
            # Because we use here partial descriptions, we can now pile onto on the current graph
            # state and group the group #surface_textures we just created with the #height_texture 
            # node. Just as in the Node Editor, nodes which shall be grouped together must be at the 
            # same level in the graph. We could for example no longer group the #albedo_texture and 
            # #height_texture nodes, as they no longer have the same parent node in the graph. The
            # final result of the grouping is as follows:
            #
            #  Group "All Textures"
            #  ├── Group "Surface Textures"
            #  │   ├── Texture "albedo_texture"
            #  │   └── Texture "roughness_texture"
            #  ├── Texture "height_texture"
            #  │   ... remaining nodes of the graph ...
            {
                "$type": "Group",
                "$id": "all_textures",
                "$children": ["#surface_textures", "#height_texture"],
                "Basic/Name": "All Textures",
            },
        ]
    )

    # Another way to group nodes is to use a query to select nodes in the graph. This case is especially 
    # useful when we have an existing graph where we might not know the IDs of the nodes we want to 
    # group together. In this case we would just load an existing graph with maxon.GraphDescription.GetGraph
    # and then omit the first partial description that creates the graph from scratch.
    maxon.GraphDescription.ApplyDescription(
        # We create the same graph as before.
        maxon.GraphDescription.GetGraph(name="Query Texture Groups"), [
            {
                "$type": "Output",
                "Surface -> outColor": {
                    "$type": "OpenPBR Material",
                    "Base/Color": {
                        "$type": "Texture",
                        "Image/Filename/Path": "asset:///file_eb62aff065c50a2b",
                    },
                    "Specular/Roughness": {
                        "$type": "Texture",
                        "Image/Filename/Path": "asset:///file_8bf49bb0b9992dbe",
                    },
                    "Geometry/Bump Map": {
                        "$type": "Bump Map",
                        "Input": {
                            "$type": "Texture",
                            "Image/Filename/Path": "asset:///file_e706df60a3a533d2",
                        },
                    },
                },
            },
            # We use a query to select all Texture nodes in the graph and group them together. We
            # can use here queries of any complexity, for example to group all that are indirectly
            # connected to a specific node. When we use a query, we cannot use the "$children" field
            # at the same time.
            {
                "$type": "Group",
                "$queryflags": maxon.GraphDescription.QUERY_FLAGS.MATCH_ALL,
                "$query": { # A very simple query that matches all nodes of type Texture in the graph.
                    "$type": "Texture", 
                },

                # Set attributes of the group node as usual.
                "Basic/Name": "Textures Selected by Query",
                "Basic/Comment": "This group was created by a query that selected all Texture nodes.",
            },
        ]
    )


def InputGroup() -> None:
    """Creates a group node with dynamically declared input and output ports.

    Input groups are useful when a graph needs a small, reusable interface whose ports are declared 
    by the graph description rather than by a node template.
    """
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Input Group"), [
            # Define the inout group start node for the graph, this will be the UI of the material
            # when selected in the material manager.
            {
            "$inputgroup": {

                # The ID of the group with which we can reference the group in the graph description.
                # "inputs" will also be the default ID when we do not provide one.
                "$id": "inputs",

                # Now we describe the ports of the input group. They will be created as both input 
                # and output ports of the group node, so that they can be connected to other nodes 
                # in the graph.
                "$ports": {

                    # A color port with a default value of white.
                    "Color 1": {
                        "$type": "color",
                        "$default": (1, 1, 1),
                    },

                    # A color port with a default value of black.
                    "Color 2": {
                        "$type": "color",
                        "$default": (0, 0, 0),
                    },

                    # An integer port with an enum associated with it. An enum means that the port
                    # can only take the listed values and will be displayed as a dropdown in the UI.
                    # These are the noise types of the Redshift Maxon Noise node, the values can be
                    # taken from the node space index.
                    "Noise Type": {
                        "$type": "int",
                        "$default": 23,
                        "$enum": {
                            "Ober": 15,
                            "Nutous": 14,
                            "Box noise": 1,
                            "Sema": 19,
                            "Cranal": 5,
                            "Blistered turbulence": 2,
                            "Displaced turbulence": 7,
                            "Pezo": 16,
                            "Dents": 6,
                            "Hama": 9,
                            "VL noise": 22,
                            "Stupl": 20,
                            "Naki": 12,
                            "FBM": 8,
                            "Turbulence": 21,
                            "Fire": 31,
                            "Poxo": 17,
                            "Noise": 13,
                            "Buya": 3,
                            "Mod noise": 11,
                            "Cell noise": 4,
                            "Luka": 10,
                            "Wavy turbulence": 23,
                            "Cell voronoi": 24,
                            "Displaced voronoi": 25,
                            "Sparse convolution": 26,
                            "Voronoi 1": 27,
                            "Voronoi 2": 28,
                            "Voronoi 3": 29,
                            "Electric": 32,
                            "Gaseous": 33,
                            "Ridged Multi Fractal": 34
                        },
                    },

                    # A vector port with a default value of (1, 1, 1).
                    "Scale": {
                        "$type": "vector",
                        "$default": (1, 1, 1),
                    },

                    # And finally a float port with a default value of 0.2, a step of 0.05, and a 
                    # min/max range of 0.0 to 1.0.
                    "Metalness": {
                        "$type": "float",
                        "$default": 0.5,
                        "$min": 0.0,
                        "$max": 1.0,
                        "$step": 0.05,
                    },

                    "Height": {
                        "$type": "float",
                        "$default": 0.25,
                        "$min": 0.0,
                        "$max": 1.0,
                        "$step": 0.05,
                    }
                },

                # An input group can have its attributes set just like any other node.
                "Basic/Name": "Input Group",
                "Basic/Comment": "This is a group node with dynamically declared input and output ports.",

            },
        },
        # Now create a second partial description that uses the input group we just defined. We can 
        # reference the input group ports using the "#inputs" syntax (which is shorthand for a graph
        # query).
        {
            "$type": "Output",

            "Surface -> outColor": {

                # The OpenPBR Material has its color and specular roughness driven by a noise node, 
                # which in turn uses the input group ports as its parameters.
                "$type": "OpenPBR Material",
                "Base/Color": {
                    "$type": "Maxon Noise",
                    "$id": "noise_node",

                    "General/Type -> Noise Type": "#inputs",
                    "General/Color 1 -> Color 1": "#inputs",
                    "General/Color 2 -> Color 2": "#inputs",
                    "Input/Scale -> Scale": "#inputs"
                },
                "Specular/Roughness": "#noise_node",

                "Base/Metalness -> Metalness": "#inputs",

                "Geometry/Bump Map": {
                    "$type": "Bump Map",

                    "Input Map Type": 1,
                    "Height Scale -> Height": "#inputs",
                    "Input": "#noise_node",
                },
            },
        }
        ]
    )

def MyCallback(scope: dict) -> dict:
    """Hides every node preview and colors Texture node title bars before their scopes are applied.
    """
    scope["Basic/Show Preview"] = False
    if scope.get("$type", None) == "Texture":
        scope["Basic/Color"] = (0.25, 0, 0)
    return scope


def DescriptionCallbacks() -> None:
    """Applies a nested material graph after MyCallback customizes each of its scopes.
    """
    # Description callbacks are functions that are called for each scope in a graph description 
    # before the description is applied to the graph. They can be used to modify the scope, which
    # can make it easier to carry out reoccurring tasks, such as setting a specific attribute on 
    # all nodes of a certain type, or to generally apply attributes, such as setting the "Show 
    # Preview" attribute to False for all nodes in a graph.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Callback Example"), 
        # The description of the graph ...
        {
            "$type": "Output",
            "Surface": {
                "$type": "OpenPBR Material",
                "Base/Metalness": 1.,
                "Base/Color": {
                    "$type": "TriPlanar",
                    "Coordinates/Scale": 0.2,
                    "Texture/Image X": {
                        "$type": "Texture",
                        "Basic/Name": "Tex: Base Color",
                        "Image/Filename/Path": "asset:///file_dcd3db0487f2def6"
                    }
                },
                "Specular/Roughness": {
                    "$type": "Scalar Ramp",
                    "Input/Alt Input": {
                        "$type": "TriPlanar",
                        "Coordinates/Scale": 0.2,
                        "Texture/Image X": {
                            "$type": "Texture",
                            "Basic/Name": "Tex: Reflection Roughness",
                            "Image/Filename/Path": "asset:///file_2e316c303b15a330"
                        }
                    }
                }
            }
        # ... and the callback function that is called for each scope.
        }, callback=MyCallback)


def main() -> None:
    """Creates all basic example graphs in the active document.
    """
    SimpleGraphDescription()
    CommentedSimpleGraphDescription()
    GettingGraphs(doc)
    LazyLiterals()
    ScopesAndReferencedNodes()
    ExplicitConnections()
    PartialDescriptions()
    GroupingNodes()
    InputGroup()
    DescriptionCallbacks()


if __name__ == "__main__":
    main()
