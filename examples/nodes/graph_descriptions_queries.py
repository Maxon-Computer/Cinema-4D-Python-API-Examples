"""Demonstrates graph description queries, including lazy color and vector literals.

Builds literal, comparison, composition, color and vector, regular-expression, nested, and
port-selection queries, then evaluates the selected queries against every Redshift material graph
in the document.

Warning:
    This script reads a c4d file in relation to itself. When you just copy and paste the example into
    the script editor, or move this file without also moving the example file, the script will not 
    work. Load this file via "File > Open Script..." from the SDK into the script manager.

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

import os
import c4d
import maxon

doc: c4d.documents.BaseDocument # The active document.

def EvaluateQueryExample() -> None:
    """Demonstrates a simple full case of using a query to select nodes.
    """
    # Most query syntax examples in this file abstract away the boiler plate code of getting the graph
    # of something and evaluating a query against it. This example shows the full process.
    
    # Get the first material in the document and its Redshift material graph.
    material: c4d.BaseMaterial = doc.GetFirstMaterial()
    graph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        material, maxon.NodeSpaceIdentifiers.RedshiftMaterial)

    # Run a simple query that selects all nodes of type "OpenPBR Material" with a Base/Weight 
    # value of 0.5.
    result: list[maxon.NodesNodeRef] = maxon.GraphDescription.EvaluateQuery(graph,
        # A query as shown in the syntax examples. This could also appear in a "$query" field of a 
        # graph description (to then select these nodes for modification), but here we just use it 
        # as a standalone query.                          
        {
            "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,
            "$type": "OpenPBR Material",
            "Base/Weight": 0.5
        }
    )

    print(f"Found {len(result)} matches: {result}")


def ApplyDescriptionExample() -> None:
    """Demonstrates cases of using a queries inside graph descriptions to select nodes for modification.
    """
    # Get the first material in the document and its Redshift material graph.
    material: c4d.BaseMaterial = doc.GetFirstMaterial()
    if material is None:
        print("No material found in the document.")
        return

    graph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        material, maxon.NodeSpaceIdentifiers.RedshiftMaterial)

    # Use a query to select all Texture nodes in a graph with a Custom Gamma value of 1.0 and set 
    # their Custom Gamma value to 2.2. ApplyDescription supports the exact same query syntax as 
    # EvaluateQuery in all its complexity with one exception: ApplyDescription does not support 
    # queries that select ports, as it makes no sense to apply a description to a port.
    maxon.GraphDescription.ApplyDescription(
        graph, {
            "$query": {
                # Here we define that this query scope is meant to match everything ...
                "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,
                # ... that has the properties defined here ...

                "$type": "Texture",         # Is a Texture node ...
                "Image/Custom Gamma": 1.0, # ... and has a Custom Gamma value of 1.0.

            },
            # ... so that we can set the gamma value of all matching nodes to 2.2.
            "Image/Custom Gamma": 2.2
        }
    )


def BasicQuerySyntax() -> dict[str, dict]:
    """Demonstrates the most basic form of a query, which is a literal value query.
    """
    # This is the most simply form of a query, testing for a literal value. We also use the shorthand
    # form which does not specify a query operator (and with that use the default equality operator). 
    query_literal: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

        # Match all nodes of type "OpenPBR Material" ...
        "$type": "OpenPBR Material",

        # ... which also have a Base/Weight value of 0.5.
        "Base/Weight": 0.5
    }

    # Queries do not have to target a specific node type, they can also be anonymous, i.e., they can 
    # just search for any node that fulfills the query conditions. Here we search for any node type
    # that has a Base/Weight input port or attribute that is set to 0.5.
    anonymous_query_literal: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

        # Match all nodes that have a Base/Weight parameter with a value of 0.5.
        "Base/Weight": 0.5
    }

    return {"query_literal": query_literal, "anonymous_query_literal": anonymous_query_literal}


def QueryOperatorSyntax() -> dict[str, dict]:
    """Demonstrates the use of comparison operators in queries.
    """
    # But queries can also take more complex forms. One level of complexity is to use a dictionary 
    # instead of a literal value, which allows us to specify a query operator explicitly.

    # Match all nodes that have a Base/Weight value equal to 0.5. This is the same as the 
    # anonymous_query_literal example but here we explicitly specify the equality operator.
    query_comp_equal: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

        "Base/Weight": {
            "$qop": "==",
            "$qvalue": 0.5
        }
    }

    # Other query operators for numeric values are: "!=", "<", "<=", ">", ">=". For string values, 
    # the operators are: "==", "!=", "regex", "regex_match" (see RegexQuerySyntax for examples).

    # Match all nodes that have a Base/Diffuse Roughness value not equal to 0.0.   
    query_comp_not_equal: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

        "Base/Diffuse Roughness": {
            "$qop": "!=",
            "$qvalue": 0.0
        }
    }

    # Match all nodes that have a Base/Weight value smaller than 0.5.
    query_comp_less: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

        "Base/Weight": {
            "$qop": "<",
            "$qvalue": 0.5
        }
    }

    # Match all nodes that have a Base/Weight value smaller than or equal to 0.5.
    query_comp_less_equal: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

        "Base/Weight": {
            "$qop": "<=",
            "$qvalue": 0.5
        }
    }

    # Match all nodes that have a Base/Weight value greater than 0.5.
    query_comp_greater: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

        "Base/Weight": {
            "$qop": ">",
            "$qvalue": 0.5
        }
    }

    # Match all nodes that have a Base/Weight value greater than or equal to 0.5.
    query_comp_greater_equal: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

        "Base/Weight": {
            "$qop": ">=",
            "$qvalue": 0.5
        }
    }

    return {"query_comp_equal": query_comp_equal, "query_comp_not_equal": query_comp_not_equal,
            "query_comp_less": query_comp_less, "query_comp_less_equal": query_comp_less_equal,
            "query_comp_greater": query_comp_greater, "query_comp_greater_equal": query_comp_greater_equal}


def CompositionQuerySyntax() -> dict[str, dict]:
    """Demonstrates the use of composition queries, which combine multiple conditions for a single port or attribute.
    """
    # The next level of complexity is to compose multiple conditions for a single port or attribute.
    # This is called a composition query. Technically, composition could contain other composition 
    # queries, but this is rarely useful in practice. 

    # This will match any node that has a Base/Weight that is larger than or equal to 0.25, smaller than
    # or equal to 1.0, and not equal to 0.5. Since we do not specify an operator for the composition, it
    # defaults to "and".
    query_comp_and: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

        # As usual we declare the port or attribute we want to query for.
        "Base/Weight": {

            # But instead of defining a query operator and value, we define a composition query, 
            # with "$qcomp". "Base/Weight" must now either fullfill all of the conditions in the 
            # composition query or at least one of them.

            "$qcomp": {

                # The mode with which the queries are composed together. 'and' is the default, we
                # therefore could also omit this line. So, in this case we indicate that all conditions 
                # must be fulfilled instead of at least one.
                "$qop": "and",

                # The three conditions of this composition which must be met. You can choose any keys
                # for the conditions, but they must be unique within the composition query.
                "0": {
                    "$qvalue": 0.25, # The Base/Weight value must be larger than or equal to 0.25.
                    "$qop": ">="
                },
                "1": {
                    "$qvalue": 1.0, # The Base/Weight value must be smaller than or equal to 1.0.
                    "$qop": "<="
                },
                "2": {
                    "$qvalue": 0.5, # The Base/Weight value must not be equal to 0.5.
                    "$qop": "!="
                }
            }
        }
    }

    # This is an or-composition query, i.e., it will match any node that has a Base/Weight that
    # is either exactly 0.25 or exactly 0.5.
    query_comp_or: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

        "Base/Weight": {
            "$qcomp": {
                "$qop": "or",
                "a": {
                    "$qvalue": 0.25, # The Base/Weight value must be equal to 0.25.
                    "$qop": "=="
                },
                "b": {
                    "$qvalue": 0.5, # OR the Base/Weight value must be equal to 0.5.
                    "$qop": "=="
                }
            }
        }
    }

    return {"query_comp_and": query_comp_and, "query_comp_or": query_comp_or}


def VectorQuerySyntax() -> dict[str, dict]:
    """Demonstrates the use of vector queries, which can be used to query for color and vector values.
    """
    # We search for all OpenPBR Material nodes in a graph that have a Base/Color value of (1, 0, 0).
    # This query looks harmless but there is more to it. When the document from which the queried
    # graph is taken from is an OCIO color managed document (which is the default since 2026), then
    # the colors stored by a node will be actually in Render Space, and not in sRGB space, which is 
    # what the user usually sees in the UI in color pickers. Graph description queries automatically 
    # unpack color values from sRGB space to Render Space before carrying out the comparison. So, we
    # are looking here for all OpenPBR Material nodes that have a Base/Color value that is equivalent 
    # to (1, 0, 0) in sRGB space, which is roughly the same as (0.6131, 0.0702, 0.0206) in Render Space.
    # For non-OCIO color managed documents, the query will just compare the literal values.
    query_simple_color: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

        "$type": "OpenPBR Material",
        "Base/Color": (1, 0, 0)
    }

    # The same query as query_simple_color, but as raw query, i.e., no implicit unpacking of color
    # values to sRGB space is done, tested will be the raw stored render space value.
    #
    # We also use "$qmaxerr" which allows us to specify a tolerance value for numeric comparisons. 
    # When not explicitly set, the default tolerance is 1E-6, which is usually sufficient for most 
    # cases. But since we here only provide values with four significant digits, and Render Space 
    # values tend to have a lot of places after the comma, we have to increase the  tolerance to 
    # 1E-3, otherwise the query might not match nodes. You can also use "$qmaxerr" for scalar 
    # queries to finetune the tolerance of the numeric comparisons.
    query_raw_color: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL |
                  maxon.GraphDescription.QUERY_FLAGS.RAW_COLORS,
        "$qmaxerr": 1E-3,

        "$type": "OpenPBR Material",
        "Base/Color": (0.6131, 0.0702, 0.0206)
    }

    # Finally, vector and color queries can also support <, <=, >, >= operators (and of course also 
    # != and ==). vec1 < vec2 means that all components of vec1 are smaller than or equal to the 
    # corresponding components of vec2, and at least one component is smaller. Similarly, vec1 <= 
    # vec2 means that all components of vec1 are smaller than or equal to the corresponding components 
    # of vec2. 

    # We use it here to find all Ramps that have a Knot.1 Color which is larger than or equal to 
    # (0.25, 0.25, 0.1) and smaller than or equal to (1, 1, 1). These operations again happen in 
    # sRGB space, despite the fact that the stored values are (usually) in Render Space.
    query_comp_color: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

        "$type": "Ramp",
        "Ramp/Knot.1/Color": {
            "$qcomp": {
                "a": {
                    "$qvalue": (.25, .25, .1),
                    "$qop": ">="
                },
                "b": {
                    "$qvalue": (1, 1, 1),
                    "$qop": "<="
                }
            }
        }
    }

    return {"query_simple_color": query_simple_color, "query_raw_color": query_raw_color,
            "query_comp_color": query_comp_color}


def RegexQuerySyntax() -> dict[str, dict]:
    """Demonstrates the use of regular expression queries, which can be used to query for string values.
    """
    # Cinema 4D uses the C++ std::regex library for regex queries. All queries are run with the 
    # ECMAScript regex grammar, which is the default grammar of std::regex. For more information on 
    # the syntax, see https://en.cppreference.com/w/cpp/regex/ecmascript.

    # Find all nodes nodes whose name contains the string "bump". "$qop": "regex" is a regex search
    # (opposed to a regex match) and only a subset of the string must match the regex.
    query_regex_search: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

        "Basic/Name": {
            "$qop": "regex",
            "$qvalue": "bump"
        }
    }

    # A similar regex search query, but this time we search for all Texture nodes whose Path starts 
    # with the given path (the "^" at the beginning of the regex indicates that the match must start 
    # at the beginning of the string). We also make use of implicit URL unpacking, which allows us 
    # to query for the UI of a an URL instead of the raw stored URL.
    query_regex_search_url: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

        "$type": "Texture",
        "Path": {
            "$qop": "regex",
            "$qvalue": "^assetdb:///Textures/Surfaces/Redshift/Leather"
        }
    }

    # With QUERY_FLAGS.RAW_URLS we can turn off the implicit URL unpacking and query for the raw 
    # stored URL instead of the UI. Other than for lazy literals, where we can just write any URL
    # form, we have here to explicitly turn off the implicit unpacking, otherwise the query will not 
    # match.
    query_regex_search_raw_url: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL |
                  maxon.GraphDescription.QUERY_FLAGS.RAW_URLS,

        "$type": "Texture",
        "Path": {
            "$qop": "regex",
            "$qvalue": "asset:///file_9e5ecffcde53576d"
        }
    }

    # Finally, a regex match query, which requires the entire string to match the regex. Here we 
    # search for all Texture nodes whose Path ends with ".jpg" (the "$" at the end of the regex 
    # indicates the end of the string). Without the "(.*)" which consumes all characters before the 
    # ".jpg", this query would not match anything, as the regex would require the string to be 
    # exactly ".jpg" which is usually not the case for a Path. For a "$qop": "regex" we could also
    # just write ".jpg" without the "(.*)", as a regex search only requires a substring to match.
    query_regex_match: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

        "$type": "Texture",
        "Path": {
            "$qop": "regex_match",
            "$qvalue": "(.*)(\\.jpg)$"
        }
    }
    return {"query_regex_search": query_regex_search,
            "query_regex_search_url": query_regex_search_url,
            "query_regex_search_raw_url": query_regex_search_raw_url,
            "query_regex_match": query_regex_match}


def ConnectionQuerySyntax() -> dict[str, dict]:
    """Demonstrates the use of connection queries, which can be used to query for nodes that are 
    connected to other nodes.
    """
    # Before we only made queries that only looked at the properties of a single node. But we can 
    # also make queries that involve the connections of a node to other nodes. The syntax should
    # com naturally to you when you have come this far with graph descriptions.

    # A nested query that selects a Bump Blender node where the indirectly connected texture nodes
    # are named "data" and "height". This query will return the Bump Blender node as we do not 
    # specify any explicit selection.
    query_connection: dict = {

        # Match all nodes of type "Bump Blender" that:
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,
        "$type": "Bump Blender",

        # 1st condition: ... has a node connected to its Layer 0/Bump Input port ...
        "Layer 0/Bump Input": {
            # ... that is a Bump Map node ...
            "$type": "Bump Map",
            # ... whose Texture/Input port is connected to a Texture node named "data".
            "Texture/Input": {
                "$type": "Texture",
                "Basic/Name": "data"
            }
        },

        # 2nd condition: Similar, but here the texture node must be named "height".
        "Layer 1/Bump Input": {
            "$type": "Bump Map",
            "Texture/Input": {
                "$type": "Texture",
                "Basic/Name": "height"
            }
        }
    }

    # A feature of connection queries is that we can select any of the connected nodes, not just the 
    # root node of the query. This is done by setting QUERY_FLAGS.SELECT_THIS on the connected nodes.

    # A similar connection query as query_connection, but this time we select nodes in the query. We
    # also make use of a few other advanced query features, such as a composition query for the name 
    # of the second texture node.
    query_connection_select_this: dict = {
        # Match all nodes of type "Bump Blender" that match the conditions below. But instead of 
        # returning the root node of the query, we will return the selected connected nodes instead.
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,
        "$type": "Bump Blender",

        "Layer 0/Bump Input": {
            "$type": "Bump Map",
            "Texture/Input": {
                "$type": "Texture",

                # Make this texture node part of the query result. As soon as we set #SELECT_THIS,
                # the root of the query will no longer be implicitly added to the result. But we could
                # still manually add it by writing ...
                #
                # "$qmode": (maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL | 
                #            maxon.GraphDescription.QUERY_FLAGS.SELECT_THIS)
                #
                # in the "Bump Blender" scope, but we do not do that here.
                "$qmode": maxon.GraphDescription.QUERY_FLAGS.SELECT_THIS,

                "Basic/Name": "data"
            }
        },

        "Layer 1/Bump Input": {
            "$type": "Bump Map",
            "Texture/Input": {
                "$type": "Texture",
                # Also select this texture node as part of the query result.
                "$qmode": maxon.GraphDescription.QUERY_FLAGS.SELECT_THIS,

                "Basic/Name": {
                    "$qcomp": {
                        "$qop": "or",
                        "a": {
                            "$qvalue": "height",
                            "$qop": "=="
                        },
                        "b": {
                            "$qvalue": "relief",
                            "$qop": "=="
                        }
                    }
                }
            }
        }
    }

    # The "$qselports" query argument allows us not only to select nodes but also ports. This is 
    # only relevant for queries with GraphDescription.EvaluateQuery, for embedded queries with 
    # GraphDescription.ApplyDescription, this will lead to errors, as the query result will then 
    # contain ports and not nodes, which is not supported by ApplyDescription because it makes 
    # conceptually no sense to apply a description to a port.
    #
    # Port queries can be useful when you want blend the Nodes and Graph Description API.
    query_port_selections: dict = {
        "$qmode": maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL,

        # When the query below is matched, we add the ports Layer 0/Blend Weight and Layer 1/Blend 
        # Weight to the query result. Just as for SELECT_THIS, this will prevent the implicit
        # root node addition to the query result. The position of this field in the scope is always
        # irrelevant, you could also place it after the conditions below.
        "$qselports": {
            # Select the Layer 0/Weight port. Just as for query compositions, the key of the 
            # dictionary is arbitrary, but must be unique. The value must be either label reference 
            # as shown here or a node path (in relation to the true node that is selected by the 
            # query).
            "0": "Layer 0/Blend Weight",
            "1": "Layer 1/Blend Weight"
        },

        # A relatively simple query that selects a Bump Blender node when when it has a bump map
        # connected to its Layer 0 and Layer 1 Bump Input ports.
        "$type": "Bump Blender",
        "Layer 0/Bump Input": {
            "$type": "Bump Map"
        },
        "Layer 1/Bump Input": {
            "$type": "Bump Map",

            # Also add the height scale port of this texture node to the query result. 
            "$qselports": {
                "0": "Inputs/Texture/Height Scale"
            }
        },
    }

    return {"query_connection": query_connection, 
            "query_connection_select_this": query_connection_select_this,
            "query_port_selections": query_port_selections}


def RunQuerySyntaxExamples() -> None:
    """Runs all query syntax examples and prints the results to the console.
    """
    queries: dict[str, dict] = {}
    queries.update(BasicQuerySyntax())
    queries.update(QueryOperatorSyntax())
    queries.update(CompositionQuerySyntax())
    queries.update(VectorQuerySyntax())
    queries.update(RegexQuerySyntax())
    queries.update(ConnectionQuerySyntax())

    for key, query in queries.items():
        print(f'{"-" * 80}\n\nQuery: {key}\n{query}\n{"-" * 80}')
        for material in doc.GetMaterials():
            graph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
                material, maxon.NodeSpaceIdentifiers.RedshiftMaterial)
            items: list[maxon.GraphNode] = maxon.GraphDescription.EvaluateQuery(graph, query)
            print(f"  '{material.GetName()}': {[str(item.GetId()) for item in items]}")


def main() -> None:
    """Evaluates the selected query examples for every Redshift material graph in the active document.
    """
    # Load the document named "graph_descriptions_queries.c4d" next to this file.
    path: str = os.path.join(os.path.dirname(__file__), "graph_descriptions_queries.c4d")
    if not os.path.exists(path):
        print(
            f"Document 'graph_descriptions_queries.c4d' not found. Please read the header of the script.")
        return
    
    if doc.GetDocumentName() != "graph_descriptions_queries.c4d":
        c4d.documents.LoadFile(path)

    # Run the simple full example.
    EvaluateQueryExample()

    # Build a dictionary of all queries.
    queries: dict[str, dict] = {}
    queries.update(BasicQuerySyntax())
    queries.update(QueryOperatorSyntax())
    queries.update(CompositionQuerySyntax())
    queries.update(VectorQuerySyntax())
    queries.update(RegexQuerySyntax())
    queries.update(ConnectionQuerySyntax())
    c4d.ClearPythonConsole()

    # Iterate over all queries and evaluate them against every Redshift material graph in the document.
    for key, query in queries.items():
        print(f'{"-" * 80}\n\nQuery: {key}\n{query}\n{"-" * 80}')
        for material in doc.GetMaterials():
            graph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
                material, maxon.NodeSpaceIdentifiers.RedshiftMaterial)
            items: list[maxon.GraphNode] = maxon.GraphDescription.EvaluateQuery(graph, query)
            print(f"  '{material.GetName()}': {[str(item.GetId()) for item in items]}")

    print("Done.")


if __name__ == "__main__":
    main()
