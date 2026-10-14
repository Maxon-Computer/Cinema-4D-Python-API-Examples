"""Demonstrates how to work with user data parameters.

You can run this example in the Script Manager of Cinema 4D. It creates a null object with an angle
slider and a direction dropdown, and then prints the configured user data to the console.

Topics:
    - Defining user data descriptions
    - Setting user data values
    - Iterating over user data
    - Removing user data
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0.0"
__date__ = "07/09/2026"

import c4d
import mxutils


doc: c4d.documents.BaseDocument # The active Cinema 4D document.
op: c4d.BaseObject | None # The currently selected object, can be None.


def main() -> None:
    """Runs the example.
    """
    # Created a null object and a float slider between 0° and 180° and a dropdown with the labels
    # "Up", "Down", "Left", and "Right".
    null: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Onull))
    doc.InsertObject(null)
    doc.SetActiveObject(null)

    # Setup the name, unit and custom GUI for the angle parameter.
    angle: c4d.BaseContainer = c4d.GetCustomDataTypeDefault(c4d.DTYPE_REAL)
    angle[c4d.DESC_NAME] = "Angle"
    angle[c4d.DESC_UNIT] = c4d.DESC_UNIT_DEGREE
    angle[c4d.DESC_CUSTOMGUI] = c4d.CUSTOMGUI_REALSLIDER

    # Set the min, max, step and default value of the parameter. Even though the unit is called 
    # degree, the underlying value is in radians.
    angle[c4d.DESC_MIN] = c4d.utils.DegToRad(0)
    angle[c4d.DESC_MAX] = c4d.utils.DegToRad(180)
    angle[c4d.DESC_STEP] = c4d.utils.DegToRad(0.5)
    angle[c4d.DESC_DEFAULT] = c4d.utils.DegToRad(90)

    # Setup the name, default, value, and cycle for the direction parameter.
    direction: c4d.BaseContainer = c4d.GetCustomDataTypeDefault(c4d.DTYPE_LONG)
    direction[c4d.DESC_NAME] = "Direction"
    direction[c4d.DESC_DEFAULT] = 0

    cycle: c4d.BaseContainer = c4d.BaseContainer()
    cycle[0] = "Up"
    cycle[1] = "Down"
    cycle[2] = "Left"
    cycle[3] = "Right"
    direction[c4d.DESC_CYCLE] = cycle

    # Add the custom parameters to the null object. The function will return a DescID for each added 
    # parameter. (ID_USERDATA, 1) and (ID_USERDATA, 2) respectively for angle and direction, because
    # user data IDs start from 1.
    didAngle: c4d.DescID = null.AddUserData(angle) 
    didDirection: c4d.DescID = null.AddUserData(direction)

    # We can now also read back the parameters, with GetUserDataContainer which works very similar to
    # Description iteration. Note that the values are here again read-only.
    for descid, data in null.GetUserDataContainer():
        print(f"{data[c4d.DESC_NAME]}")

    # Write values to our new parameters.
    null[didAngle] = c4d.utils.DegToRad(45)  # Set angle to 45°
    null[didDirection] = 3  # Set direction to "Right"

    # We could also manually define the IDs like this:
    null[c4d.ID_USERDATA, 1] = c4d.utils.DegToRad(45)  # Set angle to 45°
    null[c4d.ID_USERDATA, 2] = 3  # Set direction to "Right"

    # Remove the user data parameters from the null object.
    # null.RemoveUserData(didAngle)
    # null.RemoveUserData(didDirection)
    
    # Notify Cinema 4D that the document and its managers should refresh their views.
    c4d.EventAdd()


if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
