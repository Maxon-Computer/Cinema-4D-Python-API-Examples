# animation

Animation, keyframes, motion, and tracks.

## Files
| File | Description |
| --- | --- |
| [README.md](README.md) | This file. |
| [key_quaternion_interpolation.py](key_quaternion_interpolation.py) | Checks the interpolation of the first key for an object's rotation track. If the interpolation is linear (SLERP) it is changed to cubic. |
| [motion_tracker_object_track.py](motion_tracker_object_track.py) | Loops through all the tracks of the active Motion Tracker object. |
| [object_find_best_euler_angle.py](object_find_best_euler_angle.py) | Checks the rotation tracks of the active object. |
| [object_quaternion_rotation.py](object_quaternion_rotation.py) | Checks if the active object uses quaternion interpolation. |
| [object_sync_vector_keys.py](object_sync_vector_keys.py) | Synchronizes the keys for the tracks of the active cube's "Size" parameter. |
| [object_vector_curves.py](object_vector_curves.py) | Reads the vector components curves of the active object's rotation track curve. |
| [object_vector_tracks.py](object_vector_tracks.py) | Reads the vector components tracks of the active object's position track curve. |
| [track_copy.py](track_copy.py) | Copies the position, rotation and animation Tracks (so all Keyframes) from obj1 to obj2. |
| [track_create_keys.py](track_create_keys.py) | Creates position Y tracks. Adds two keyframes. Sets their value and interpolation. |
| [track_synchronized.py](track_synchronized.py) | Checks if the rotation track of an object is synchronized. If not, it will be synchronized. |

## Related Examples

| Type | Example | Description |
| --- | --- | --- |
| Script | [modata_get_selection](simulation/modata_get_selection.py) | Retrieves all selected clones of the active Cloner object. |
| Script | [objects](../scene/objects.py) | Demonstrates basic operations on objects. |
