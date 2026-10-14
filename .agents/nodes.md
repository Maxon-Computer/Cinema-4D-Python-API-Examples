# Nodes Documentation

Cinema 4D provides two ways to describe scene and material content: With the Cinema API centering around `c4d.BaseList2D`, realizing things such as `c4d.BaseObject` or `c4d.BaseTag`, and with the Nodes API centering around `maxon.GraphNode`. This document describes high level concepts of the Nodes API and how to use it to create node graphs.

# TOC

- [APIs](#apis): Describes the two main APIs for creating node graphs.
- [Concepts](#concepts): Describes the main concepts of the Nodes API.
- [Rules](#rules): Describes the rules for creating graphs with the Nodes API and Graph Description API.
- [Examples](#examples): Provides examples of how to use the Nodes API and Graph Description API.
- [Skills](#skills): Provides a list of skills that are useful for working with the Nodes API.

# APIs

Within the nodes system exists two main APIs:

- **Nodes API**: This is the native API for creating and manipulating node graphs. It is fairly complex and requires a good understanding of the underlying concepts. It usually also leads to more verbose (longer) code.
- **Graph Description API**: This is a higher level API that allows users to describe node graphs in a more artist-friendly way. Other than the Nodes API, Graph Descriptions also offer a query syntax and multiple convenience features such as implicitly converting sRGB colors to render space colors. There are however also some more technical things that are only possible with the Nodes API.

## Choose an API

- For node materials, use the Graph Description API by default instead of writing Nodes API code. Use the Nodes API only when the user explicitly requests it or when the requested operation cannot be expressed with Graph Descriptions. If the user has named an API, follow that request.
- For Scene Nodes (Neutron), always use the Nodes API. Do not ask whether to use Graph Description API, and do not implement Scene Nodes with Graph Descriptions.

# Concepts

- **Node Spaces**: A node space is a collection of node types that can be used to create node graphs. Node spaces are usually tied to a specific renderer or other system. For example, the Redshift node space contains all the nodes that are available for creating Redshift materials. The node spaces shipped with Cinema 4D are:
  - **Redshift Render**: This is the material node space for Redshift and by far the most popular node space in Cinema 4D. When users ask you to do something, they will likely want you to operate in this space (but might not explicitly say so).
  - **Standard Render**: This is the material node space for the Standard Renderer. It is not as popular as Redshift, but it is still used by many users.
  - **Scene Nodes**: This is an alternative to the Cinema API for describing scene content. The code name of scene nodes is Neutron.
  - You can find meta data for node spaces in `.agents/nodespaces/_overview.md`. This will by default include all information about the three node spaces named above. 
  - Users can also dump node space information for third party renderers such as VRay or Arnold and overwrite the default information. They might also accidentally provide an incomplete node space dump. When you do not find any node space information for the default node spaces, report to the user that they likely provided an incomplete node space dump.
- **Node Templates**: The definition of node types are stored as *node templates* in the asset databases. As an agent, you will likely not need to interact with these templates directly and asset databases directly, as you have access to `.agents/nodespaces/_overview.md` which will provide you with all the information you need about nodes. See `.agents/assets.md` for an abstracted overview of the Asset API.
  - **Node Graphs**: Node graphs contain a set of nodes and connections between them. Node graphs are represented by the type `maxon.GraphModelInterface` (whose instance is named `maxon.GraphModelRef`). In practice you will often also deal with the specialization `maxon.NodesGraphModelInterface` (whose instance is named `maxon.NodesGraphModelRef`) which provides a few additional functions. For current API details, start at <https://developers.maxon.net/docs/py> and search for `Nodes Framework`.
- **Nodes**: Elements in a node graph are represented by the type `maxon.GraphNode`. Although named 'node', this type does not represent only things that a user would consider a node, but also ports, groups and more. The term *node* in `maxon.GraphNode` refers to the tree structure with which such graph nodes are arranged.

# Rules

- Avoid abstraction such as a `CreateFooNode()` function. The creation of a material should happen in one function.
- Describe each graph with one complete, literal dictionary, including its nested nodes and connections. Do not build the graph by assembling dictionary fragments or calling helper functions.
- Use absolute filesystem paths unless the user explicitly requests relative paths. Write paths literally instead of constructing them with `os.path.join()`.
- Provide high level commentary for graph descriptions and Nodes API code that roughly summarizes what the code does.

# Examples

These are examples relevant to the Nodes API and Graph Description API.

## Graph Description API

These examples demonstrate general principles of the Graph Description API and are not tied to a specific node space or concrete task.

- [Graph Descriptions Basics](../examples/nodes/graph_descriptions_basics.py): Demonstrates how graph descriptions create and modify node graphs.
- [Graph Descriptions References](../examples/nodes/graph_descriptions_references.py): Demonstrates how graph descriptions resolve node and port references.
- [Graph Descriptions Queries](../examples/nodes/graph_descriptions_queries.py): Demonstrates how graph descriptions select nodes and ports in material graphs.
- [Graph Descriptions Commands](../examples/nodes/graph_descriptions_commands.py): Demonstrates how to carry out common node and port operations using graph description commands.
- [Graph Descriptions Callbacks and Types](../examples/nodes/graph_descriptions_callbacks_and_types.py): Demonstrates how graph description callbacks and data types work.

# Skills

## Graph Description API

### Redshift

Browse [Redshift Node Space](nodespaces/com_redshift3d_redshift4c4d_class_nodespace/_overview.md) to discover Redshift node types, their ports, and their properties.

The following are full skills, i.e., skills that describe a complete Redshift material graph. They can be used as is to create a complete material graph.

- [Open PBR Material](../examples/nodes/skills/full_gd_rs_openpbrmaterial.md): Describes a generic Redshift Open PBR material graph using the Graph Description API.

The following are partial skills, i.e., skills that describe a specific aspect of a Redshift material graph and not a complete material graph. Combine them to create a complete material graph.

- [Texture](skills/nodes/part_gd_rs_texture.md): Describes how to use textures in Redshift material graphs.
- [Bump](skills/nodes/part_gd_rs_bump.md): Describes how to use bump maps in Redshift material graphs.
- [Ramps](skills/nodes/part_gd_rs_ramps.md): Describes how to use ramp nodes to remap values or create gradients in Redshift material graphs.
