# Redshift Ramp Nodes Skill

Demonstrates using the ramps in Redshift material graphs.

Skill `part_gd_rs_ramps.md`:
- `part`: Describes a partial material or scene graph.
- `gd`: Uses the Graph Description API to create the graph.
- `rs`: Is tied to the Redshift node space.

Search for the node template "Ramp" in `.agents/nodespaces` to find the node template description and discover all 
the ports and properties of the Redshift Ramp node. Search for "Scalar Ramp" to find the node template description 
of the Redshift Scalar Ramp node.

## Skill

Redshift offers two ramp types: A scalar ramp node which is a single channel ramp and a ramp node which is a 
multi-channel ramp. The user sees the scalar-ramp as a spline GUI and the ramp node as a gradient ramp GUI. Scalar ramps 
are often used to tweak grey scale textures and values such as bump maps, roughness maps, metalness maps, etc. And Ramps 
are often used to recolor textures and values. Both Scalar Ramps and Ramps can also be used without an input and then act
like a gradient generator. 

### Scalar Ramp

```py
# A scalar ramp node is put in the between a scalar output port and a scalar input port. Scalar ramps can also be connected 
# to color output ports and color input ports, but the output of a scalar ramp is always a single/grey channel value.
{
    "$type": "OpenPBR Material",

    # Connect the Base/Metalness input port of the Open PBR Material node to a Ramp node.
    "Base/Metalness": {
        "$type": "Scalar Ramp",

        # Ramps use the concept of variadic ports, i.e., the number of spline points is not fixed and can be changed by 
        # the user. We therefore have to set the number of points in the ramp before we can set the values of the points. 
        # The default number of points is 2 (in which case this command would not be needed).
        "$commands": {
            # Set the variadic port "Points" to have 3 three children. The referenced port must be marked as isVariadic 
            # in the node template meta data for this command to work. We could also just write "Ramp/Points" using a 
            # lazy reference.
            "$cmd_set_port_count": { "General/Ramp/Ramp/Points": 3 } 
        },

        # We could also write "General/Ramp/Ramp/Points/Point.0/Position X" below but we use lazy references which are 
        # shorter and easier to read. Variadic ports usually start counting with .1. You can deduced the port names from
        # the default child ports expressed in the node template meta data. 

        # We set the three points to where we want them to be and the desired interpolation mode.
        "Point.1/Position X": 0.0,
        "Point.1/Position Y": 0.0,
        "Point.1/Interpolation": "cubic",
        "Point.2/Position X": 0.5,
        "Point.2/Position Y": 0.25,
        "Point.2/Interpolation": "cubic",
        "Point.3/Position X": 1.0,
        "Point.3/Position Y": 1.0,
        "Point.3/Interpolation": "cubic",

        # Both Ramp and Scalar Ramp nodes also have a builtin noise feature which helps making the ramp less uniform. A
        # Frequency of 0.25 will yield relatively large noise patterns, a frequency of 2.0 will yield smaller noise patterns.
        # And frequencies above 5.0 will yield very small noise patterns.
        "Adjust/Noise Amount": 0.25, # The smaller the value, the less noise is added to the ramp.
        "Adjust/Noise Frequency": 0.25, # The larger the value, the smaller the noise patterns are.

        # The source for the ramp which is value remapped, in this case a texture node.
        "Input": {
            "$type": "Texture",
            "Image/Filename/Path": maxon.Url("file:///C:/your/path/to/your/metalness_tex.png")
        },
    },
}
```

### Ramp

```py
# A ramp node is put in the between a color output port and a color input port.
{
    "$type": "OpenPBR Material",

    # Connect the Base/Color input port of the Open PBR Material node to a Ramp node.
    "Base/Color": {
        "$type": "Ramp",

        # Set the variadic port "Ramp" to have five children. The referenced port must be marked as isVariadic 
        # in the node template meta data for this command to work. We could also just write "Ramp/Ramp" using a 
        # lazy reference. And yes, the variadic port of a ramp node has the label path "General/Ramp/Ramp" and 
        # not "General/Ramp/Ramp/Knots" as one might expect, probably a bit of an oversight.
        "$commands": {
            "$cmd_set_port_count": { "General/Ramp/Ramp": 5 } # Set the variadic port "General/Ramp/Ramp" to have 5 points.
        },

        # We set the offset and color of the five points and the desired interpolation mode.
        "Knot.1/Color": (1, 0, 0), # Red
        "Knot.1/Bias Position": 0.0,
        "Knot.1/Interpolation": "cubic",
        "Knot.2/Color": (0, 1, 0), # Green
        "Knot.2/Bias Position": 0.25,
        "Knot.2/Interpolation": "cubic",
        "Knot.3/Color": (0, 0, 1), # Blue
        "Knot.3/Bias Position": 0.5,
        "Knot.3/Interpolation": "cubic",
        "Knot.4/Color": (1, 1, 0), # Yellow
        "Knot.4/Bias Position": 0.75,
        "Knot.4/Interpolation": "cubic",
        "Knot.5/Color": (1, 1, 1), # White
        "Knot.5/Bias Position": 1.0,
        "Knot.5/Interpolation": "cubic",

        # Both Ramp and Scalar Ramp nodes also have a builtin noise feature which helps making the ramp less uniform. A
        # Frequency of 0.25 will yield relatively large noise patterns, a frequency of 2.0 will yield smaller noise patterns.
        # And frequencies above 5.0 will yield very small noise patterns.
        "Adjust/Noise Amount": 0.25, # The smaller the value, the less noise is added to the ramp.
        "Adjust/Noise Frequency": 0.25, # The larger the value, the smaller the noise patterns are.

        # The source for the ramp which is value remapped, in this case a texture node.
        "Input": {
            "$type": "Texture",
            "Image/Filename/Path": maxon.Url("file:///C:/your/path/to/your/color_tex.png"),
        },
    },
}