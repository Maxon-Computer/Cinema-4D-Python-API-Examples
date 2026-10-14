"""Demonstrates graph description commands.

Each example creates a graph in a known state and then modifies it with a command. The examples
reset, disconnect, hide or show selected ports, remove nodes, and change variadic-port counts
while using ordinary Python tuples for color port values. They also demonstrate start and solo
node commands, as well as dissolving nested groups with one-level and recursive ungroup commands.

Note:
    This example is written for the Redshift Material nodes, it will only work when you have
    Redshift installed. But the same principles will also work in any other node space, such as
    Standard Render, Vray, Arnold, etc.
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__date__ = "29/07/2026"
__license__ = "Apache-2.0 License"
__version__ = "2027.0.0"

import c4d
import maxon

def CommandBasics() -> None:
    """Demonstrates the basic usage of graph description commands.
    """
    # Description commands are a way to apply modifications to an existing graph that go beyond
    # setting values and connections. A command is always being applied to a node and signaled by 
    # a "$commands" field in the node's scope.
    graph1: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(name="Command Basics 1")
    maxon.GraphDescription.ApplyDescription(graph1,
            {   
                # Create a very simple graph with an Output node and an OpenPBR Material node 
                # connected to it. The "$commands" field in the OpenPBR Material node's scope will 
                # hide all ports of that node.
                "$type": "Output",
                "Surface": {
                    "$type": "OpenPBR Material",

                    "$id": "material",
                    "Base/Color": (1, 0, 0),
                    "$commands": "$cmd_hide_ports"
                }
            }
    )

    # What we have done above is however a shorthand form. As the field name "$commands" implies,
    # you can also apply multiple commands to a node. In this more complex form, we can also specify 
    # an explicit list of ports to which the command should be applied.
    graph2: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(name="Command Basics 2")
    maxon.GraphDescription.ApplyDescription(
            graph2,
            {   
                "$type": "Output",
                "Surface": {
                    "$type": "OpenPBR Material",

                    "$id": "material",
                    "Base/Color": (1, 0, 0),
                    # Run two commands on the OpenPBR Material node, one to hide two ports, and one 
                    # to show one of them again.
                    "$commands": {
                        "$cmd_hide_ports": ["Base/Color", "Specular/Color"],
                        "$cmd_show_ports": ["Base/Color"],
                    }
                }
            }
    )

    # Finally, commands are often used in with queries on existing graphs. Here we for example show
    # the "Base/Color" port of #graph1 again.
    maxon.GraphDescription.ApplyDescription(graph1,
        {
            "$query": "#material",
            "$commands": {
                "$cmd_show_ports": ["Base/Color"],
            },
        }
    )

def DefaultingNodes() -> None:
    """Demonstrates how to reset a node to its default values using a graph description command.
    """
    # A pair of graph descriptions, where the first creates a graph, and the second resets the 
    # OpenPBR Material in that graph to its default values. We use here the feature of partial 
    # descriptions (see graph_descriptions_basics.py), i.e., an ApplyDescription call that applies 
    # multiple descriptions to the same graph to emulate having an existing graph which we modify 
    # with a command. The "$commands": "$cmd_default" instruction could also be put into the 
    # "OpenPBR Material" scope of the first description, with the same effect. But commands are 
    # often applied as shown here. We have some kind of existing graph, we query for one to many 
    # nodes in it, and then apply commands to those nodes.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Default Command"), [
        # Create the 'Hello World' graph.
        {
            "$type": "Output",
            "Surface": {
                "$type": "OpenPBR Material",
                "$id": "material",
                "Base/Color": (1, 0, 0),
                "Base/Metalness": 1.0,
                "Specular/IOR": 3.14159,
            }
        },
        # Query for the OpenPBR Material node and apply the $cmd_default command to it, which resets
        # all the changes we made to it in the first description.
        {
            "$query": "#material",
            "$commands": "$cmd_default"
        }
    ])

    # The command can also target an explicit list of input ports instead of applying to all ports.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Default Explicit Command"), [
        {
            "$type": "Output",
            "Surface": {
                "$type": "OpenPBR Material",
                "$id": "material",
                "Base/Color": (1, 0, 0),
                "Base/Metalness": 1.0,
                "Specular/IOR": 3.14159,
            }
        },
        {
            "$query": "#material",
            "$commands": {
                "$cmd_default": ["Base/Color", "Base/Metalness"],
            },
        }
    ])


def DisconnectingNodes() -> None:
    """Demonstrates how to disconnect a matched node from every connected port.
    """
    # A pair of graph descriptions, where the first creates the 'Hello World' graph, and the
    # second disconnects the OpenPBR Material node in that graph from the rest of the graph.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Disconnect Command"), [
        # Create the 'Hello World' graph.
        {
            "$type": "Output",
            "Surface": {
                "$type": "OpenPBR Material",
                "$id": "material",
                "Base/Color": (1, 0, 0),
                "Base/Metalness": 1.0,
                "Specular/IOR": 3.14159,
            }
        },
        # Query for the OpenPBR Material node and apply and disconnect all its connections.
        {
            "$query": "#material",
            "$commands": "$cmd_disconnect"
        }
    ])

    # The command can also target an explicit list of ports instead of disconnecting every port.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Disconnect Explicit Command"), [
        {
            "$type": "Output",
            "Surface": {
                "$type": "OpenPBR Material",
                "$id": "material",
                "Base/Color": {
                    "$type": "Noise",
                },
                "Specular/Color": {
                    "$type": "Noise",
                },
            }
        },
        {
            "$query": "#material",
            "$commands": {
                "$cmd_disconnect": ["Base/Color"],
            },
        }
    ])


def ShowingAndHidingPorts() -> None:
    """Demonstrates how port visibility commands interact with explicitly described connections.
    """
    # A slightly changed "Hello World!" graph which connects a Noise node to the Reflection Color
    # port of an OpenPBR Material, hides all ports of the OpenPBR Material, and shows all ports of
    # the Noise node. This is a case where it makes sense to use a command while creating a new 
    # graph, so we only need one description here.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Visibility Command"), [
        {
            "$type": "Output",
            # An OpenPBR Material node connected to the "Surface" port of the Output node where all
            # ports are hidden in the OpenPBR Material except for the port connections we explicitly
            # describe here ('outColor' and 'Specular/Color'). Note that the explicit out port
            # reference in 'Surface -> outColor' is not necessary, we just use it to make the example
            # more verbose. Also note that just setting values without a connection (as in 'Base/Color')
            # will not cause a port to be shown when all ports have been hidden before.
            "Surface -> outColor": {
                "$type": "OpenPBR Material",
                "$commands": "$cmd_hide_ports",

                "Base/Color": (1, 0, 0),
                # A Noise node connected to the 'Specular/Color' of the OpenPBR Material where all
                # ports are shown. This will affect both input and output ports. But this will have
                # no effect on the number of variadic ports a node has.
                "Specular/Color": {
                    "$type": "Noise",
                    "$commands": "$cmd_show_ports"
                }
            }
        }
    ])

    # Visibility commands can target an explicit list of ports. Here we hide two ports and then
    # show one of them again.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Visibility Explicit Command"), [
        {
            "$type": "Output",
            "Surface": {
                "$type": "OpenPBR Material",
                "$id": "material",
                "Base/Color": (1, 0, 0),
                "$commands": {
                    "$cmd_hide_ports": ["Base/Color", "Specular/Color"],
                },
            }
        },
        {
            "$query": "#material",
            "$commands": {
                "$cmd_show_ports": ["Base/Color"],
            },
        }
    ])


def RemovingNodes() -> None:
    """Demonstrates how to permanently remove a matched node from an existing graph.
    """
    # A pair of graph descriptions, where the first creates the 'Hello World' graph, and the
    # second deletes the OpenPBR Material from that graph, leaving only the the Output node.
    # This example is a bit clinical, as it makes usually little sense to first create a node, 
    # and then delete it again within a single application of graph descriptions. This command 
    # is intended to be used in the context of graphs loaded from a material stored in an existing 
    # scene.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Remove Command"), [
        # Create the 'Hello World' graph.
        {
            "$type": "Output",
            "Surface": {
                "$type": "OpenPBR Material",
                "$id": "material",
                "Base/Color": (1, 0, 0),
                "Base/Metalness": 1.0,
                "Specular/IOR": 3.14159,
            }
        },
        # Query for the OpenPBR Material node and remove it from the graph.
        {
            "$query": "#material",
            "$commands": "$cmd_remove"
        }
    ])


def SettingPortCounts() -> None:
    """Demonstrates how to grow, shrink, or uniformly set a node's variadic-port count.
    """
    # Applies a simple description that adds an RS Scalar Ramp node to the graph.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="SetPortCount 3 Command"), {
            "$type": "Scalar Ramp",
        # Explicitly set the point count of the ramp to three (adding one point from its default of
        # two). #cmd_set_port_count will only add or remove as many points as necessary. We can there
        # also use it to ensure that port has exactly N children.
            "$commands": {
                "$cmd_set_port_count": {
                    "Ramp/Ramp/Points": 3,
                },
            },

            "Point.1/Position X": 0.0,
            "Point.1/Position Y": 0.0,
            "Point.1/Interpolation": "cubic",
            "Point.2/Position X": 0.5,
            "Point.2/Position Y": 0.25,
            "Point.2/Interpolation": "cubic",
            "Point.3/Position X": 1.0,
            "Point.3/Position Y": 1.0,
            "Point.3/Interpolation": "cubic",
        })

    # We can also use the same syntax to remove points. Here we will end up with constant 50% grey ramp.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="SetPortCount 1 Command"), {
            "$type": "Scalar Ramp",
            "$commands": {
                "$cmd_set_port_count": {
                    "Ramp/Ramp/Points": 1,
                },
            },

            "Point.1/Position Y": 0.5
        })

    # An empty port target list applies the command to all variadic ports of the node, which at least
    # for most Redshift Nodes is the same as the explicit variant as they only have one variadic port.
    # For the Scalar Ramp node, this is exactly the same as the previous example, as that none has only
    # one variadic port, the "Ramp/Ramp/Points" port.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="SetPortCount All Command"), {
            "$type": "Scalar Ramp",
            "$commands": {
                "$cmd_set_port_count": 1,
            },
        })


def SettingStartAndSoloNodes() -> None:
    """Demonstrates how to set the start and solo nodes with graph description commands.
    """
    # Creates a simple graph where the color of an OpenPBR Material is driven by a Noise node. The 
    # Noise node is set as the start node, i.e., the node that will be shown by default in the 
    # Attribute Manager when the graph/material is selected.
    graph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(name="Start Command")
    maxon.GraphDescription.ApplyDescription(graph, {
        "$type": "Output",
        "Surface -> outColor": {
            "$type": "OpenPBR Material",
            "Base/Color": {
                "$type": "Noise",
                "$commands": "$cmd_set_start"
            },
        },
    })

    # Same thing, but this time we set the Noise node as the solo node, i.e., mute all output of the
    # graph except for the output of the Noise node.
    graph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(name="Solo Command")
    maxon.GraphDescription.ApplyDescription(graph, {
        "$type": "Output",
        "Surface -> outColor": {
            "$type": "OpenPBR Material",
            "Base/Color": {
                "$type": "Noise",
                "$commands": "$cmd_set_solo"
            },
        },
    })

    # Finally, there also exist the inverse commands to clear the start and solo nodes, respectively.
    # An important technical insight for start and solo nodes is that always only one can exist for
    # a given graph. So, setting two start nodes or two solo nodes will always result in the last 
    # one being the effective one. In inverse this also means that we can call the clear command on
    # any node in the graph and it will still clear the "correct" node.
    graph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(name="Clear Solo Command")
    maxon.GraphDescription.ApplyDescription(graph, [

        # First we create a description which solos the noise node.
        {
            "$type": "Output",
            "Surface -> outColor": {
                "$type": "OpenPBR Material",
                "Base/Color": {
                    "$type": "Noise",
                    "$commands": "$cmd_clear_solo"
                },
            },
        },
        # And now we clear the solo state again. Since we did not set an explicit ID for the Noise 
        # node, we make use of the fact that we can clear the solo/start state on any node in the 
        # graph, so we simply pick the Output node to clear it there. We pick the output node because
        # we know there is always exactly one output node in a graph, so this little snippet would
        # work for any material.
        {
            "$query": {
                "$type": "Output"
            },
            "$commands": "$cmd_clear_solo"
        }
    ])

    

def UngroupingNodes() -> None:
    """Creates nested groups and dissolves them again with ungroup commands.
    """
    # A graph description for a material with three textures, where two of them are grouped into a 
    # "Surface Textures" group, and the third one is grouped together with the first group into an 
    # "All Textures" group.
    description: list[dict] = [
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
        {
            "$type": "Group",
            "$id": "surface_textures",
            "$children": ["#albedo_texture", "#roughness_texture"],
            "Basic/Name": "Surface Textures",
        },
        {
            "$type": "Group",
            "$id": "all_textures",
            "$children": ["#surface_textures", "#height_texture"],
            "Basic/Name": "All Textures",
        }
    ]

    # Add one material for comparison, which we will not modify with any ungroup commands.
    # graph0: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(name="Ungroup Command (unmodified)")
    # maxon.GraphDescription.ApplyDescription(graph0, description)

    # Create a new material with this description.          
    graph1: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(name="Ungroup Command (ID)")
    maxon.GraphDescription.ApplyDescription(graph1, description)

    # Now we non-recursively ungroup the #all_textures group, which will dissolve that group but 
    # leave the inner #surface_textures group intact.
    maxon.GraphDescription.ApplyDescription(graph1, [
        {
            "$query": "#all_textures",
            "$commands": "$cmd_ungroup",
        }
    ])

    # Rinse and repeat, but this time we will recursively ungroup the #all_textures group, which 
    # will dissolve that group and the inner #surface_textures group as well.
    graph2: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(name="Ungroup Command (ID - Recursive)")
    maxon.GraphDescription.ApplyDescription(graph2, description)
    
    maxon.GraphDescription.ApplyDescription(graph2, [
        {
            "$query": "#all_textures",
            "$commands": "$cmd_rec_ungroup",
        }
    ])

    # Finally, we could of course also use other qualifiers than IDs to identify what to dissolve.
    # Note that the ungroup command will throw an error when you try to ungroup a node that is not a 
    # group, so for non-ID queries we should always at least check the type.
    graph3: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(name="Ungroup Command (Type)")
    maxon.GraphDescription.ApplyDescription(graph3, description)

    maxon.GraphDescription.ApplyDescription(graph3, [
        {
            "$query": {
                # Make the query match multiple nodes (ALL), but do not throw an error when there 
                # are no matches at all (MAYBE). There are multiple query flags, see the query 
                # documentation for details.
                "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

                "$type": "Group",                # Target all groups in the graph ...
                "Basic/Name": {                  # ... whose name ends with "Textures".
                    "$qop": "regex",
                    "$qvalue": ".*Textures$"
                }

            },
            "$commands": "$cmd_ungroup",
        }
    ])


if __name__ == "__main__":
    CommandBasics()
    DefaultingNodes()
    DisconnectingNodes()
    ShowingAndHidingPorts()
    RemovingNodes()
    SettingPortCounts()
    SettingStartAndSoloNodes()
    UngroupingNodes()
    c4d.EventAdd()
