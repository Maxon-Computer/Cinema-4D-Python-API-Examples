# Redshift Open PBR Material Skill

Demonstrates how to create a Redshift Open PBR material graph using the Graph Description API. Remove comments and 
change the texture paths and relevant values when generating materials for users.

Skill `full_gd_rs_openpbrmaterial.md`:
- `full`: Describes a full material or scene graph.
- `gd`: Uses the Graph Description API to create the graph.
- `rs`: Is tied to the Redshift node space.

## Important

- Make sure to include a Bump Map node between the texture and the Geometry/Bump Map input of the Open PBR Material node.
- There should be usually at least a color correction setup between the texture and the Base/Color input of the Open PBR Material node. 

## Skill

```py
import c4d
import maxon

doc: c4d.documents.BaseDocument  # The active document.

def main() -> None:
    """Creates a Redshift Open PBR material graph.
    """
    # Create a material named Open PBR and get its Redshift material graph.
    graph: maxon.NodesGraphModelRef = maxon.GraphDescription.GetGraph(
        name="Open PBR", maxon.NodeSpaceIdentifiers.RedshiftMaterial)

    # Apply a graph description to the graph that describes a common Open PBR material setup.
    maxon.GraphDescription.ApplyDescription(
        graph, {
            # The end node of the graph is an Output node.
            "$type": "Output",

            # Connect the Output->Surface input port to a Redshift Open PBR  material node.
            "Surface": {
                "$type": "OpenPBR Material",

                # --- Base (Diffuse) Section ---------------------------------------------------------------------------

                # This section more or less has to be defined for each material, especially the diffuse/color channel 
                # and the metalness channel. We use for both channels a texture node, but one could also set a literal 
                # value for both channels.

                "Base/Color": {
                    "$type": "Texture",
                    "Image/Filename/Path": maxon.Url("file:///C:/your/path/to/your/color_tex.png"),
                },
                # "Base/Color": (1, 0, 0),  # This would set the color to red.

                # Defined must also always be the metalness of the material. A metallic material should 
                # have a metalness of 1.0, a non-metallic material should have a metalness of 0.0.
                "Base/Metalness": {
                    "$type": "Texture",
                    "Image/Filename/Path": maxon.Url("file:///C:/your/path/to/your/metalness_tex.png"),
                },
                # "Base/Metalness": 1.0, # This would set the metalness to 1.0, making the material strongly metallic.

                # The diffuse roughness is a less commonly set channel as it is often replaced by the 
                # specular roughness channel. 
                "Base/Roughness": {
                    "$type": "Texture",
                    "Image/Filename/Path": maxon.Url("file:///C:/your/path/to/your/diffuse_roughness_tex.png"),
                },
                # "Base/Roughness": 0.5, # This would be a material that is neither very rough nor very smooth.

                # --- Specular Section ---------------------------------------------------------------------------------

                # Specular data is also a required input for an Open PBR material.

                # Sets the specular color to white (the default). Setting this to a texture or a color other than white 
                # is quite unusual.
                "Specular/Color": (1, 1, 1),

                # The specular roughness is a required input for an Open PBR material. It can be set to a texture or a 
                # literal value.
                "Specular/Roughness": {
                    "$type": "Texture",
                    "Image/Filename/Path": maxon.Url("file:///C:/your/path/to/your/specular_roughness_tex.png"),
                },
                # "Specular/Roughness": 0.5, # This would be a material that is neither very rough nor very smooth.

                # Set the IOR of the material, this will also impact the transmission IOR. The default value is 1.5, 
                # which is a good value for most materials. Commonly used values are: Air: 1.0003, Water: 1.33, Glass: 
                # 1.5, Metals: 2.0 - 6.0, Wood: 1.5 - 1.7, Skin: 1.3 - 1.5, Plastic: 1.3 - 1.7, Diamond: 2.4.
                "Specular/IOR": 1.5,

                # --- Transmission Section -----------------------------------------------------------------------------

                # This entire section is optional and only required for materials that are fully or partially transparent.

                # Other than for the base (diffuse) and specular component, the transmission weight is not set to 1 by
                # default but 0. So, in order to see the effect, you need to set it to a value greater than 0.
                "Transmission/Weight": 1.0,

                # Set the transmission color with either a texture or color literal.
                "Transmission/Color": {
                    "$type": "Texture",
                    "Image/Filename/Path": maxon.Url("file:///C:/your/path/to/your/transmission_color_tex.png"),
                },
                # "Transmission/Color": (1, 1, 1), # This would set the transmission color to white.

                # --- Geometry Section ---------------------------------------------------------------------------------

                # This entire section is optional and only required for materials that have a bump, normal, or alpha channel.

                # When the material contains an alpha channel, the opacity of the material can be set here.
                "Geometry/Opacity": {
                    "$type": "Texture",
                    "Image/Filename/Path": maxon.Url("file:///C:/your/path/to/your/opacity_tex.png"),
                },

                # Define a bump or normal map for the material.
                "Geometry/Bump Map": {
                    "$type": "Bump Map",

                    # The type of the bump map. Possible values are: 0: Height Field, 1: Tangent-Space Normal, 
                    # 2: Object-Space Normal.
                    "Input Map Type": 0,

                    # The strength of the effect. 1.0 is quite strong, 0.1 is a subtle effect.
                    "Height Scale": .2,
                    "Input": {
                        "$type": "Texture",
                        "Image/Filename/Path": maxon.Url("file:///C:/your/path/to/your/bump_map_tex.png"),
                        "Scale": "#texTransform"
                    }
                }
            }

            # --- Displacement Section ---------------------------------------------------------------------------------

            # Displacement is not part of the material model but must be set in the output node.
            "Displacement": {
                "$type": "Displacement",

                # TODO (Ferdinand): Fill in Inputs/Texture/Map Encoding, Inputs/Texture/Space Type, etc.

                # Set the displacement texture.
                "Texture/TexMap": {
                    "$type": "Texture",
                    "Image/Filename/Path": maxon.Url("file:///C:/your/path/to/your/displacement_tex.png"),
                    "Scale": "#texTransform"
                }
            },
        }
    )

if __name__ == "__main__":
    main()
```