# nodes

Node-based workflows, node graphs, and node materials.

## Files
| File | Description |
| --- | --- |
| [README.md](README.md) | This file. |
| [graph_descriptions_basics.py](graph_descriptions_basics.py) | Demonstrates how graph descriptions create and modify node graphs. |
| [graph_descriptions_commands.py](graph_descriptions_commands.py) | Demonstrates graph description commands. |
| [graph_descriptions_queries.c4d](graph_descriptions_queries.c4d) | No short description provided. |
| [graph_descriptions_queries.py](graph_descriptions_queries.py) | Demonstrates graph description queries, including lazy color and vector literals. |
| [graph_descriptions_references.py](graph_descriptions_references.py) | Demonstrates graph description references together with lazy color and URL literals. |
| [nodes_associate_nodes.py](nodes_associate_nodes.py) | Demonstrates how to associate nodes in a Maxon API graph with their corresponding Cinema 4D API surrogate elements. |
| [nodes_create_or_get_graphs.py](nodes_create_or_get_graphs.py) | Demonstrates creating or getting node graphs in a scene. |
| [nodes_graph_entities.py](nodes_graph_entities.py) | Demonstrates the inner structure of node graphs and how to find entities in them. |
| [nodes_group.py](nodes_group.py) | Retrieve the selected node material and group the node that are selected. |
| [nodes_info.py](nodes_info.py) | Retrieve information about the selected port of a selected material. |
| [nodes_material_access.py](nodes_material_access.py) | Demonstrates accessing node materials and their graph contents in a scene. |
| [nodes_material_create_redshift.py](nodes_material_create_redshift.py) | Demonstrates setting up a Redshift node material composed out of multiple nodes. |
| [nodes_material_standard.py](nodes_material_standard.py) | Demonstrates setting up a Standard renderer node material composed out of multiple nodes. |
| [nodes_modify_port.py](nodes_modify_port.py) | Create a material for the standard node space and modify the value of the BDSF color port. |
| [nodes_selection.py](nodes_selection.py) | This example shows how to select different elements on a node graph. It creates a node material, select ports, print connections and select wires. |
| [nodes_solo.py](nodes_solo.py) | This example shows how to solo a node. It creates a material and solo's the end node in this material. |
| [nodes_wire_mute.py](nodes_wire_mute.py) | Retrieve the selected node material and toggle-mute the selected connection, i.e., if the connection is muted, it will be unmuted or vice-versa. A connection is composed out of eight wires, to mute the connection, one must set the INHIBIT wire to WIRE_MODE.NORMAL. To unmute the connection, one must set the INHIBIT wire to WIRE_MODE.REMOVE. |
| [xpresso_create_connect.py](xpresso_create_connect.py) | Creates a Constants and Results node in the Xpresso Tag of the selected object. Connects both Nodes together. |
| [xpresso_delete.py](xpresso_delete.py) | Deletes the first node created from the Xpresso Tag of the selected object. |
| [xpresso_from_tag.py](xpresso_from_tag.py) | Retrieves the Node Master (The BaseList2D object that holds all nodes) from an Xpresso Tag. |
| [xpresso_iterate.py](xpresso_iterate.py) | Loops through all nodes from the Xpresso Tag of the selected object. Checks if it's a Constant Node. |
| [xpresso_move.py](xpresso_move.py) | Moves the first node in the Graph View created from the Xpresso Tag of the selected object. |

## Related Examples

| Type | Example | Description |
| --- | --- | --- |
| Script | [objects](../scene/objects.py) | Demonstrates basic operations on objects. |
| Script | [ocio](../rendering/ocio.py) | Demonstrates how to read, write, and convert colors in an OpenColorIO (OCIO) color-managed document in Cinema 4D. |
