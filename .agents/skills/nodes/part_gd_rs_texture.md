# Redshift Texture Node Skill

Demonstrates using the Texture node in Redshift material graphs.

Skill `part_gd_rs_texture.md`:
- `part`: Describes a partial material or scene graph.
- `gd`: Uses the Graph Description API to create the graph.
- `rs`: Is tied to the Redshift node space.

Search for the node template "Texture" in `.agents/nodespaces` to find the node template description and discover all 
the ports and properties of the Redshift Texture node.

## Skill

```py
# The singular output port of a texture node is a color port and can be connected to any color input 
# port of a Redshift material node.
{
    "$type": "OpenPBR Material",

    # Connect the Base/Color input port of the Open PBR Material node to a texture node.
    "Base/Color": {
        "$type": "Texture",

        # Set the texture path to a texture file on disk.
        "Image/Filename/Path": maxon.Url("file:///C:/your/path/to/your/texture.png"),

        # Or set it to a raw asset url. Users will usually not provide you with raw asset urls.
        "Image/Filename/Path": maxon.Url("asset:///file_32f8a3d55ef5aaab"),

        # Or set it to an assetdb url which is what users will see instead of a raw asset url. This
        # assetdb url describes the same asset as the raw asset url above, but is more human readable.
        "Image/Filename/Path": maxon.Url("assetdb:///Textures/Surfaces/Standard & Physical/Cork/cork_01_diffuse.jpg"),

        # --- The following settings are all optional. Only set them if a non-default value is needed.

        # The color space of the texture, the default is "auto", other possible values are "sRGB", "Raw", 
        # "scene-linear Rec.709-sRGB" or "ACEScg" (among others).
        "Image/Filename/Color Space": "raw", 

        # The texture transform.
        "Remap/Offset": (0.5, 0.5), # Default is (0, 0)
        "Remap/Scale": (0.5, 0.5), # Default is (1, 1)
        "Remap/Rotate": 45.0, # Default is 0.0
    },
}
```