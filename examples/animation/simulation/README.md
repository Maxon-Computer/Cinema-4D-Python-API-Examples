# simulation

Simulation, dynamics, particles, and fields.

## Files
| File | Description |
| --- | --- |
| [README.md](README.md) | This file. |
| [field_list_add_mask.py](field_list_add_mask.py) | Creates a FieldList with a formula layer, a mask and another formula layer used as a mask of the first formula layer. Assigns this FieldList to the active object that have a c4d.FIELDS parameter e.g. all MoGraph effectors. |
| [field_list_sampling.py](field_list_sampling.py) | Samples arbitrary points from multiple fields with c4d.FieldList and stores the result into a vertex color tag. |
| [field_object_sampling.py](field_object_sampling.py) | Samples arbitrary points within a random field. |
| [modata_get_selection.py](modata_get_selection.py) | Retrieves all selected clones of the active Cloner object. |
| [modata_get_weights.py](modata_get_weights.py) | Retrieves the weights from all clones of the active Cloner object. |
| [modata_read_color.py](modata_read_color.py) | Retrieves the color or each clone using two ways. First one by accessing directly the Mograph Data. Second one by accessing the polygon cache representation of the Mograph Cloner. |
| [modata_set_selection.py](modata_set_selection.py) | Generates and sets a MoGraph selection tag on a MoGraph cloner object. Effectively, this will create a selection tag for all uneven clones in the cloner object. This script has no runtime requirements, as it creates its inputs itself. |
| [modata_set_weights.py](modata_set_weights.py) | Sets a weight of 1.0 for all clones of the active Cloner object. |
| [particle_group_object.py](particle_group_object.py) | Demonstrates how to read particle data from a ParticleGroupObject. |
| [thinking_particles_creates.py](thinking_particles_creates.py) | Creates 90 Thinking Particles. Defines custom position and color for each particle. |
| [voronoi_fracture.py](voronoi_fracture.py) | Creates and define a noise shader as an input of a Voronoi Fracture object. |

## Related Examples

| Type | Example | Description |
| --- | --- | --- |
| Script | [geometry_polygon_object](../../modeling/geometry_polygon_object.py) | Explains the user-editable polygon object model of the Cinema API. |
| Script | [python_effector](../../scene/scripting-elements/python_effector.py) | Creates a Python Effector object that attracts clones to its origin. |
