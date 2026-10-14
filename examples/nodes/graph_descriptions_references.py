"""Demonstrates graph description references together with lazy color and URL literals.

Compares readable interface labels with absolute and lazy API identifiers, sets color and URL port
values, and addresses nested port-bundle children and dynamically created variadic-port children.

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


def LabelReferences() -> None:
    """Resolves node types and ports through unambiguous English interface labels.
    """
    # Node types, attributes and ports can be referenced through their English interface labels as
    # alternative to their absolute API identifiers. This is more readable and easier to write, but
    # we must make sure that the label references are unambiguous. For attributes and ports this
    # means that we should included the groups and section labels of where the port is located in 
    # the node's interface.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Label References"), {
            # This is a label reference to a node type.
            "$type": "Output",
            "Surface": {
                # This is also a label reference to a node type.
                "$type": "OpenPBR Material",
                # This is a label reference to an input port. We need here the "Base/" because the
                # node has more than one "Color" port.
                "Base/Color": (1, 0, 0),
                # This would be even more precise but is not required in this case. It is also legal
                # to write the same port or attribute multiple times in a description, the last 
                # value will be used (and apart from an example, it is also not very useful).
                "Base Properties/Base/Color": (1, 0, 0),
                # This is unambiguous because the "Metalness" port is unique in the node.
                "Metalness": 1.0,
                # This is not unambiguous, it will raise an error as there are many ports called
                # "Color" in this node.
                # "Color": (1, 0, 0)
            }
        }
    )


def IdentifierReferences() -> None:
    """Contrasts absolute API identifiers with shorter lazy identifier references.
    """
    # An alternative to label references are API identifiers. We can use here the absolute identifiers 
    # or lazy identifiers.

    # The description with absolute identifiers, this gets hard to read quite quickly.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Identifier References"), {
            # An output node.
            "$type": "#com.redshift3d.redshift4c4d.node.output",
            # Its surface input port.
            "#<com.redshift3d.redshift4c4d.node.output.surface": {
                # An OpenPBR Material node.
                "$type": "#com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial",
                # And its base color, metalness, and specular IOR input ports.
                "#<com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.base_color": (1, 0, 0),
                "#<com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.base_metalness": 1.0,
                "#<com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.specular_ior": 1.5
            }
        }
    )

    # The same description with lazy identifiers, this is much more readable. It is recommended
    # to include leading dots in lazy identifiers, e.g., "#~.base_color" and not "#~base_color"
    # to avoid matching against "foo.barbase_color".
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Lazy Identifier References"), {
            "$type": "#~.output",
            "#~.surface": {
                "$type": "#~.openpbrmaterial",
                # When there would be more than one port or attribute in this node which ends in
                # ".base_color" in this node, this would be ambiguous and raise an error. This can
                # especially true for port bundles and variadic ports, we would then have to make
                # the lazy identifier more specific, e.g., "#~.foo/base_color" or "#~.foo/_0/base_color".
                # But for simple ports like this, we can often just type out the last component.
                "#~.base_color": (1, 0, 0),
                "#~.base_metalness": 1.0,
                "#~.specular_ior": 1.5
            }
        }
    )


def PortBundleReferences() -> None:
    """Sets a Filename bundle child through complete and shortened nested port paths.
    """
    # Applies graph descriptions that create an RS Texture node and set the texture path.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Referencing Port Bundles (Label)"), {
            "$type": "Texture",

            # We set the #Path port of the #Filename port bundle to the URL of an asset. 'General' and
            # 'Image' are both not ports but attribute groups and this is the most verbose form of a
            # label reference.
            "General/Image/Filename/Path": "asset:///file_eb62aff065c50a2b",

            # These would all also work due to the ability of graph descriptions to lazily resolve label
            # references and the fact that in this case each of them unambiguously identifies an input port
            # in an RS Texture node.
            "Image/Filename/Path": "asset:///file_eb62aff065c50a2b",
            "Filename/Path": "asset:///file_eb62aff065c50a2b",
            "Path": "asset:///file_eb62aff065c50a2b",
        })

    # Applies graph descriptions that create an RS Texture node and set the texture path.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Referencing Port Bundles (ID)"), {
            "$type": "Texture",

            # This is the absolute API identifier reference for the #Path port in the #Filename port bundle,
            # where:
            #
            #   #                                        denotes a description identifier reference
            #   <                                        denotes an input port
            #   com.redshift3d...texturesampler.tex0     denotes the #Filename port bundle
            #   /                                        denotes a child element
            #   path                                     denotes the #Path port of the #Filename port bundle
            "#<com.redshift3d.redshift4c4d.nodes.core.texturesampler.tex0/path":
                "asset:///file_eb62aff065c50a2b",

            # We could also use lazy identifiers to shorten this, although I would not recommend using the
            # last variant as it is very ambiguous for human readers despite being technically unambiguous.
            "#~.texturesampler.tex0/path": "asset:///file_eb62aff065c50a2b",
            "#~.tex0/path": "asset:///file_eb62aff065c50a2b",
            "#~/path": "asset:///file_eb62aff065c50a2b",
        })


def VariadicPortReferences() -> None:
    """Addresses Scalar Ramp points through label and API identifier paths for variadic children.
    """
    # Applies a simple description that adds an RS Scalar Ramp node to the graph.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Referencing Variadic Ports (Label)"), {
            "$type": "Scalar Ramp",

            # Sets the Y position of the 0th point (what is shown as Point.1 in the UI). The decomposed
            # reference is:
            #
            #   Ramp            denotes the attribute group 'Ramp' in the node.
            #   Ramp            denotes the port bundle #Ramp of type 'net.maxon.render.portbundle.spline'.
            #   Points          denotes the variadic port #Points in that port bundle which holds a list
            #                    of 'net.maxon.render.portbundle.splinepoint'.
            #   Point.0         denotes the first 'splinepoint' port bundle held by the variadic port.
            #   Position Y      denotes one of the fields of a 'splinepoint' port bundle.
            "Ramp/Ramp/Points/Point.1/Position Y": 1.0,

            # For good measure we now write a few more values and at the same time demonstrate that we can
            # also use lazy references here.
            "Point.1/Position Y": 1.0,
            "Point.1/Interpolation": "linear",
            "Point.2/Position Y": 0.0,
            "Point.2/Interpolation": "linear"
        })

    # Applies a simple description that adds an RS Scalar Ramp node to the graph.
    maxon.GraphDescription.ApplyDescription(
        maxon.GraphDescription.GetGraph(name="Referencing Variadic Ports (ID)"), {
            "$type": "Scalar Ramp",

            # Sets the Y position of the 0th point. The decomposed reference is:
            #
            #   #<                          denotes an input port identifier reference in graph descriptions.
            #   com....rsscalarramp.ramp    denotes the port bundle #Ramp of type 'net.maxon.render.portbundle.spline'.
            #   points                      denotes the variadic port #Points in that port bundle which holds a list
            #                                of 'net.maxon.render.portbundle.splinepoint'.
            #   _0                          denotes the first 'splinepoint' port bundle held by the variadic port.
            #   positiony                   denotes one of the fields of a 'splinepoint' port bundle.
            "#<com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_0/positiony": 1.0,

            # For good measure we now write a few more values and at the same time demonstrate that we can
            # also use lazy references here.
            "#~_0/positiony": 1.0,
            "#~_0/interpolation": "linear",
            "#~_1/positiony": 0.0,
            "#~_1/interpolation": "linear",
        })


def main() -> None:
    """Creates all reference-resolution example graphs.
    """
    LabelReferences()
    IdentifierReferences()
    PortBundleReferences()
    VariadicPortReferences()
    c4d.EventAdd()


if __name__ == "__main__":
    main()
