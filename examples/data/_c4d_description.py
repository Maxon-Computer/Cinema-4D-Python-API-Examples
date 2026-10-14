"""Demonstrates important functions for the type c4d.Description.

A Cinema API description defines the GUI and metadata for the parameters of a scene element. It
does not store the actual values of the parameters, but things such as min, max, and default values.
While descriptions are not as important as BaseContainer and DescID for the parameter model, 
understanding them is crucial for working with parameters, especially when you want to dynamically 
modify or create them.

Topics:
    - Loading descriptions
    - Accessing parameter containers
    - Iterating over parameters
    - Debug printing descriptions
    - Handling user data
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0.0"
__date__ = "07/09/2026"

import c4d
import mxutils


doc: c4d.documents.BaseDocument # The active Cinema 4D document.
op: c4d.BaseObject | None # The currently selected object in the Cinema 4D document, can be None.


def main() -> None:
    """Runs the example.
    """
    # Instantiate a bend object and get its description.
    bend: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Obend))
    desc: c4d.Description = bend.GetDescription(c4d.DESCFLAGS_DESC_NONE)

    # A description is the GUI and data type definition for a scene element, or slightly simplified, 
    # the blueprint of the scene element. You can encounter descriptions in two manners:
    #
    #   1. Static: When you call GetDescription() on a scene element, we get a COPY of its description,
    #              i.e., all changes made to the description will not affect the original scene element.
    #
    #   2. Dynamic: When you implement a scene element ourself, you can override NodeData.GetDDescription(),
    #              where you get a read-write description that you can dynamically modify. See plugins/
    #              py_obj_dynamic_parameters.py for an example. Another context for dynamic descriptions
    #              (to a lesser extent) are user data. See the end of the example for more details.

    print("\n--- Basics ------------------------------------------------------------------------\n")

    # Descriptions can be hollow shells and the function LoadDescription() can be used to check if
    # a description has been successfully loaded. This is usually only necessary to do in 
    # GetDDescription(). For description for an already instantiated scene element, we can somewhat
    # safely assume that its description has been successfully loaded.
    if not desc.LoadDescription(c4d.Obend):
        print("Failed to load description for the bend object.")

    # We can now either iterate over the description's elements or access them individually using 
    # their IDs.

    # Get the container for the DEFORMOBJECT_SIZE parameter in the description.
    data: c4d.BaseContainer = desc.GetParameter(c4d.DescID(c4d.DEFORMOBJECT_SIZE))

    # Print the container for the DEFORMOBJECT_SIZE parameter. Each parameters container will hold
    # the gui and type configuration for the parameter. DESC_NAME is for example the name of the 
    # parameter, or DESC_MAX the maximum value for the parameter (if it supports such).
    print("Parameter container for the DEFORMOBJECT_SIZE:")
    mxutils.DebugPrint.PrintContainer(data)

    # We can also iterated over all parameters in the description using a loop.
    data: c4d.BaseContainer # The container holding the parameter data for each element in the description.
    descid: c4d.DescID # The description ID for each element in the description.
    groupid: c4d.DescID # The group ID for each element in the description.

    print("\nIterating over all parameters in the description:")
    for data, descid, groupid in desc:
        print(f"Data: {data}, DescID: {descid}, GroupID: {groupid}")
        # Because we get yielded the full descid of each element, we can also do type checks like:
        if descid[0].dtype == c4d.DTYPE_REAL:
            print("Found a REAL parameter.")

    # When you only want to debug print the description of a node, you can also DebugPrint and the
    # node itself, which will print the parameter tree and its details. It also supports many 
    # customization options, see the docs for details.
    print("\nmxutils.DebugPrint.PrintParameters(bend):")
    mxutils.DebugPrint.PrintParameters(bend)

    # As a practical example, this how we could get the labels of all dropdowns/selections (which 
    # are called cycles in Cinema API slang) in the bend object's description. Cycles are always 
    # represented by the DTYPE_LONG (integer) type, and when such integer parameters has a 
    # DESC_CYCLE attribute, it holds the mapping of IDs to their corresponding labels.
    for data, descid, _ in desc:
        if descid[0].dtype == c4d.DTYPE_LONG and data[c4d.DESC_CYCLE]:
            print(f"Found the cycle parameter '{data[c4d.DESC_NAME]}':")
            for id, label in data[c4d.DESC_CYCLE]:
                print(f"  ID: {id}, Label: {label}")

    print("\n--- Userdata ----------------------------------------------------------------------\n")

    # A special case for descriptions are user data. Cinemas will not formally give us a description
    # object but the parameter containers for the description part which holds the user data.

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

    c4d.EventAdd()

if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
