# Redshift Bump Maps Skill

Demonstrates using the bump map nodes in Redshift material graphs.

Skill `part_gd_rs_bump.md`:
- `part`: Describes a partial material or scene graph.
- `gd`: Uses the Graph Description API to create the graph.
- `rs`: Is tied to the Redshift node space.

Search for the node template "Bump Map" in `.agents/nodespaces` to find the node template description and discover all 
the ports and properties of the Redshift Bump Map node.

## Skill

Bump maps can be applied as a single layer map.
```py
# A bump map node is applied to a bump map input port of a material node. Bump maps are NOT the correct input for the
# `Displacement` input port of an Output node. See the displacement skill for that. 
{
    "$type": "OpenPBR Material",

    # The port which receives the output of the Bump Map node, in this case the Geometry/Bump Map input port of the 
    # Open PBR Material node.
    "Geometry/Bump Map": {
        "$type": "Bump Map",

        # The type of the bump map. Possible values are: 0: Height Field, 1: Tangent-Space Normal, 
        # 2: Object-Space Normal.
        "Input Map Type": 0,

        # The strength of the effect. 1.0 is quite strong, 0.1 is a subtle effect.
        "Height Scale": .2,

        # The input of the bump map node, which can be a texture node, a noise, or ramp/color correct node, etc. Or 
        # anything that outputs a single channel value. In this case we use a texture node.
        "Input": {
            "$type": "Texture",

            "Image/Filename/Path": maxon.Url("file:///C:/your/path/to/your/bump_map_tex.png"),
            "Scale": "#texTransform"
        }
    }
}
```

Or as multi-layer bump map.
```py
{
    "$type": "OpenPBR Material",

    # The port which receives the output of the Bump Map node, in this case the Geometry/Bump Map input port of the 
    # Open PBR Material node.
    "Geometry/Bump Map": {
        "$type": "Bump Blender",

        # Although Bump Blenders accept multiple layers, they do not have a variadic port for the layers. Instead, they 
        # have a base layer plus three hard coded bump layers.

        # The base layer of the layered bump map, the dominant bump layer.
        "Base/Input": {
            "$type": "Bump Map",

            "Input Map Type": 0,
            "Height Scale": .2,

            "Input": {
                "$type": "Texture",

                "Image/Filename/Path": maxon.Url("file:///C:/your/path/to/your/bump_map1_tex.png"),
                "Scale": "#texTransform"
            }
        },

        # The first additional bump layer.
        "Layer 0/Bump Input": {
            "$type": "Bump Map",

            "Input Map Type": 0,
            "Height Scale": .2,

            "Input": {
                "$type": "Texture",

                "Image/Filename/Path": maxon.Url("file:///C:/your/path/to/your/bump_map2_tex.png"),
                "Scale": "#texTransform"
            }
        },
        # ... and its weight.
        "Layer 0/Weight": 0.5,

        # The second additional bump layer.
        "Layer 1/Bump Input": {
            "$type": "Bump Map",

            "Input Map Type": 0,
            "Height Scale": .2,

            "Input": {
                "$type": "Texture",

                "Image/Filename/Path": maxon.Url("file:///C:/your/path/to/your/bump_map3_tex.png"),
                "Scale": "#texTransform"
            }
        },
        # ... and its weight.
        "Layer 1/Weight": 0.5,

        # There would also be a third additional bump layer (Layer 2) but we omit it here for brevity.
    }
}