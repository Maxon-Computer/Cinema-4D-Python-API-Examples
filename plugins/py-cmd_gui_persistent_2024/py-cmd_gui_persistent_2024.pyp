"""Demonstrates how to store dialog layout data and values persistently over dialog open/close
and Cinema 4D restart boundaries.

Open this dialog example by running the command "Py - Persistent Gui" in the Commander (Shift + C).
The dialog contains four groups whose size can be adjusted by the user, and one GUI element
in each group. The group weights and gadget values will persist when the dialog is closed
and reopened, the user switches a layout, or when Cinema 4D is restarted.

Note:

    Cinema 4D itself heavily relies on layout files these days to persistently store dialog layouts
    and values. In this regard, the API is working as intended. But third party plugins often are 
    not part of a layout file, and therefore cannot rely on the layout file system for this purpose.

    This example therefore uses custom serialization and deserialization to cover all possible 
    boundaries (open/close and restart) over which values should be preserved. This is only relevant
    for the case when the dialog is not part of a layout file.

    The relevant code sections have been marked with "@CustomSerialization", and there is also
    `py-cmd_gui_persistent_no_restart_2024.pyp` next to this example which does not use custom
    serialization and deserialization, i.e., has these sections removed. The dialog data saving 
    will work there within layouts files and within one Cinema 4D session, but not over Cinema 4D 
    restart boundaries.

Subjects:
    - Layout support for dialogs via BFM_LAYOUT_GETDATA and BFM_LAYOUT_SETDATA.
    - Using BFV_GRIDGROUP_ALLOW_WEIGHTS to allow the user to resize groups in a dialog.
    - Using GeDialog.GroupWeightsSave() and GroupWeightsLoad() to manage group weights.
    - Custom hyper file serialization and deserialization of dialog values.
"""
__copyright__ = "Copyright 2025, MAXON Computer"
__author__ = "Ferdinand Hoppe"
__date__ = "06/06/2025"
__license__ = "Apache-2.0 license"

import os
import typing

import c4d
import maxon
import mxutils

class PersistentGuiDialog(c4d.gui.GeDialog):
    """Realizes a dialog that persistently stores its group weights and a handful of values.
    """
    # The IDs for the dialog elements, these must be unique within the dialog.

    # The default border space around a group in the dialog and the default space between the
    # elements in a group.
    PAD_BORDER_SPACE: tuple[int] = (5, 5, 5, 5)
    PAD_ELEMENT_SPACE: tuple[int] = (5, 5) 

    # The default layout flags used by most elements in the dialog. SCALEFIT means that an element
    # tries to consume all available space in the dialog, and BFM_H and BFM_V are  the prefixes for
    # horizontal and vertical layout flags, respectively.
    FLAG_LAYOUT_SCALE: int = c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT
    FLAG_TOP_LEFT: int = c4d.BFH_SCALEFIT | c4d.BFV_TOP

    # The IDs for the main groups of the dialog, these are used to manage the weights.
    ID_GRP_MAIN: int = 1000
    ID_GRP_A: int = 1001
    ID_GRP_B: int = 1002
    ID_GRP_C: int = 1003
    ID_GRP_D: int = 1004
    
    # The IDs for the three labels displaying the size of groups in the main group.
    ID_LBL_WEIGHT_A: int = 1100
    ID_LBL_WEIGHT_B: int = 1101
    ID_LBL_WEIGHT_C: int = 1102
    ID_LBL_WEIGHT_D: int = 1103

    # The IDs for the persistent values we are going to store in the dialog. I.e., the values of
    # these gadgets will persist between Cinema 4D sessions.
    ID_CHK_PERSISTENT_VALUE: int = 1200 # The checkbox in ID_GRP_A
    ID_STR_PERSISTENT_VALUE: int = 1201 # The edit text in ID_GRP_B
    ID_CMB_PERSISTENT_VALUE: int = 1202 # The combo box in ID_GRP_C
    ID_NUM_PERSISTENT_VALUE: int = 1203 # The integer field in ID_GRP_D

    # The IDs for the combo box entries.
    ID_COLOR_RED: int = 0
    ID_COLOR_GREEN: int = 1
    ID_COLOR_BLUE: int = 2

    def __init__(self) -> None:
        """Initialize the dialog.
        """
        # Declare the weights and persistent field attributes of the dialog. 
        self._weights: c4d.BaseContainer | None = None
        self._chkPersistentValue: bool | None = None
        self._strPersistentValue: str | None = None
        self._cmbPersistentValue: int | None = None
        self._numPersistentValue: int | None = None

    def CreateLayout(self) -> bool:
        """Called by Cinema 4D to let the dialog populate its GUI.
        """
        self.SetTitle("Py - Persistent Gui")

        # Add the static text at the top of the dialog, that explains what the dialog does. This is
        # formally not part of the example and can be ignored.
        self.AddMultiLineEditText(
            999, c4d.BFH_SCALEFIT, inith=50,
            style=c4d.DR_MULTILINE_READONLY | c4d.DR_MULTILINE_WORDWRAP | 
                  c4d.DR_MULTILINE_NO_DARK_BACKGROUND | c4d.DR_MULTILINE_NO_BORDER)
        self.SetString(999, "Demonstrates a dialog with a persistent GUI state that will be saved "
                            "between Cinema 4D sessions. Resize the groups and change the values "
                            "then restart Cinema 4D to see the values being restored.")
        # end of helper text

        self.GroupBorderSpace(*self.PAD_BORDER_SPACE)

        # Add the 2x2 layout main group of the dialog. Because we pass #BFV_GRIDGROUP_ALLOW_WEIGHTS,
        # the user will be able to resize the groups in the main group by dragging the splitters.
        self.GroupBegin(
            self.ID_GRP_MAIN, self.FLAG_LAYOUT_SCALE, 2, 2, "", c4d.BFV_GRIDGROUP_ALLOW_WEIGHTS)

        # Add the four sub groups to of the main group for the 2*2 layout, i.e., we will end up
        # with a layout like this:
        #
        #   A | B
        #   --+---
        #   C | D
        #
        # The user will be able to drag the horizontal and vertical splitters to resize the groups
        # A, B, C, and D. The weights of the groups will be saved and restored when the dialog is
        # reopened or when Cinema 4D is restarted.

        # Add the A group, which contains a checkbox to enable or disable a persistent value.
        self.GroupBegin(self.ID_GRP_A, self.FLAG_LAYOUT_SCALE, cols=1)
        self.GroupBorderNoTitle(c4d.BORDER_THIN_IN)
        self.GroupBorderSpace(*self.PAD_BORDER_SPACE)
        self.GroupSpace(*self.PAD_ELEMENT_SPACE) 
        self.AddStaticText(self.ID_LBL_WEIGHT_A, self.FLAG_TOP_LEFT)
        self.AddCheckbox(self.ID_CHK_PERSISTENT_VALUE, self.FLAG_TOP_LEFT, 200, 0, "Enabled")
        self.GroupEnd() # end of ID_GRP_A

        # Add the B group, which contains an edit text field for a persistent value.
        self.GroupBegin(self.ID_GRP_B, self.FLAG_LAYOUT_SCALE, cols=1)
        self.GroupBorderNoTitle(c4d.BORDER_THIN_IN)
        self.GroupBorderSpace(*self.PAD_BORDER_SPACE)
        self.GroupSpace(*self.PAD_ELEMENT_SPACE) 
        self.AddStaticText(self.ID_LBL_WEIGHT_B, self.FLAG_TOP_LEFT)
        self.AddEditText(self.ID_STR_PERSISTENT_VALUE, self.FLAG_TOP_LEFT, initw=200) 
        self.GroupEnd() # end of ID_GRP_B

        # Add the C group, which contains a combo box for a persistent value.
        self.GroupBegin(self.ID_GRP_C, self.FLAG_LAYOUT_SCALE, cols=1)
        self.GroupBorderNoTitle(c4d.BORDER_THIN_IN)
        self.GroupBorderSpace(*self.PAD_BORDER_SPACE)
        self.GroupSpace(*self.PAD_ELEMENT_SPACE) 
        self.AddStaticText(self.ID_LBL_WEIGHT_C, self.FLAG_TOP_LEFT)
        self.AddComboBox(self.ID_CMB_PERSISTENT_VALUE, self.FLAG_TOP_LEFT, initw=200)
        self.AddChild(self.ID_CMB_PERSISTENT_VALUE, self.ID_COLOR_RED, "Red")
        self.AddChild(self.ID_CMB_PERSISTENT_VALUE, self.ID_COLOR_GREEN, "Green")
        self.AddChild(self.ID_CMB_PERSISTENT_VALUE, self.ID_COLOR_BLUE, "Blue")
        self.GroupEnd() # end of ID_GRP_C

        # Add the D group, which contains an integer field for a persistent value.
        self.GroupBegin(self.ID_GRP_D, self.FLAG_LAYOUT_SCALE, cols=1)
        self.GroupBorderNoTitle(c4d.BORDER_THIN_IN)
        self.GroupBorderSpace(*self.PAD_BORDER_SPACE)
        self.GroupSpace(*self.PAD_ELEMENT_SPACE) 
        self.AddStaticText(self.ID_LBL_WEIGHT_D, self.FLAG_TOP_LEFT)
        self.AddEditNumberArrows(self.ID_NUM_PERSISTENT_VALUE, self.FLAG_TOP_LEFT, initw=200)
        self.GroupEnd() # end of ID_GRP_D

        # @CustomSerialization: One of the issues at the moment is that #BFM_LAYOUT_SETDATA will not
        # have been emitted yet when we open the dialog for the first time after a restart of
        # Cinema 4D. And since #GroupWeightsLoad() will only work while the group is not yet closed
        # when the dialog is not part of a layout, we need to load the weights manually here. To
        # simplify things, we also use the #LoadValues() but pass None, to signal that we want to
        # load values from disk, which will be done in the #LoadValuesFromDisk() method. This must
        # be removed when you do not need @CustomSerialization.
        if self._weights is None:
            self.LoadValues(None)

        # Load the weights of the main group, this call must be made before the group is closed, 
        # unless we only want to operate the dialog within a layout file, then #GroupWeightsLoad()
        # could also be called somewhere else, e.g., in #InitValues().
        self.GroupWeightsLoad(self.ID_GRP_MAIN, self._weights)
        
        self.GroupEnd() # end of ID_GRP_MAIN

        return True
    
    def InitValues(self) -> bool:
        """Called by Cinema 4D to initialize the values dialog once its GUI has bee built.
        """
        # Set the persistent values of the dialog. The values cannot be None at this point.
        self.SetBool(self.ID_CHK_PERSISTENT_VALUE, self._chkPersistentValue)
        self.SetString(self.ID_STR_PERSISTENT_VALUE, self._strPersistentValue)
        self.SetInt32(self.ID_CMB_PERSISTENT_VALUE, self._cmbPersistentValue)
        self.SetInt32(self.ID_NUM_PERSISTENT_VALUE, self._numPersistentValue)

        # Set the labels display the dialog group weights.
        self.SetWeightLabels()

        return True

    def Message(self, msg: c4d.BaseContainer, result: c4d.BaseContainer) -> bool:
        """Called by Cinema 4D to handle messages sent to the dialog.
        """
        mid: int = msg.GetId() # The ID of the current message.

        # BFM_WEIGHTS_CHANGED is emitted by Cinema 4D when the weights of a group have changed,
        # i.e., when user has resized a group by dragging the splitter. Since a dialog can have
        # multiple groups with weights, we need to check which group has changed (in our case it
        # technically can only be the main group, since that is our only group with weights).
        if (mid == c4d.BFM_WEIGHTS_CHANGED and 
            msg.GetInt32(c4d.BFM_WEIGHTS_CHANGED) == self.ID_GRP_MAIN):

            # In a common implementation, you usually do not have to handle this message as, you
            # often do not have to react to the user resizing a group. But since we want to display
            # a weight label for each group, we need to update the labels when the user resizes
            # the groups

            # Get the weights of the main group, write them into the class field, and then
            # update the labels of the groups with the new weights.
            weights: c4d.BaseContainer | None = self.GroupWeightsSave(self.ID_GRP_MAIN)
            if weights is not None:
                self._weights = weights

            self.SetWeightLabels()
            return True
        
        # BFM_LAYOUT_GETDATA is emitted by Cinema 4D when it wants to get the layout data of the 
        # dialog, i.e., it is asking us to save the current layout data into the result
        # container of the message. It is VERY IMPORTANT that we set the ID of the #result
        # container to something else than `-1` as Cinema 4D will otherwise just ignore our data.
        elif (mid == c4d.BFM_LAYOUT_GETDATA):
            # Set the ID of the result container and then just use our abstraction SaveValues() to
            # save the layout data into the result container.
            result.SetId(PersistentGuiCommand.ID_PLUGIN)
            return self.SaveValues(result)
        
        # BFM_LAYOUT_SETDATA is emitted by Cinema 4D when it wants us to load some previously
        # stored layout data into the dialog. This happens for example when the user switches the
        # layout of Cinema 4D, or when the dialog has been opened. Unfortunately, this message is
        # only emitted after CreateLayout() has been called, causing all the custom serialization
        # trouble we have here. 
        elif (mid == c4d.BFM_LAYOUT_SETDATA):
            # The message data is a bit odd in that the container does not directly contain the
            # #BFM_LAYOUT_SETDATA data, but stored in a sub-container with the ID
            # c4d.BFM_LAYOUT_SETDATA. We pass this to be loaded data to our abstraction LoadValues()
            # which will then load the data in that container into the dialog.
            data: c4d.BaseContainer = msg.GetContainer(c4d.BFM_LAYOUT_SETDATA)
            return self.LoadValues(data)
                
        return c4d.gui.GeDialog.Message(self, msg, result)
    
    
    def AskClose(self) -> bool:
        """Called by Cinema 4D when the user tries to close the dialog to potentially prevent it.

        @CustomSerialization: 

            This whole method is only needed when we want to manually save layout data to disk. You
            can remove this method when you do not need @CustomSerialization.
        """
        if not self.SaveValues(None):
            print("Warning: Failed to save persistent values to disk.")

        return False # Returning False allows the dialog to be closed. Returning True would
                     # prevent the dialog from being closed, which is not what we want here.
    
    # --- Custom dialog methods for loading and saving values --------------------------------------

    def LoadValues(self, data: c4d.BaseContainer | None) -> bool:
        """Loads the layout/values container #data into their respective class fields.

        A similar method is advisable for all persistent dialogs implementations. We have implemented
        this method in a special way, as that it does not only take a BaseContainer as an argument, 
        but also allows us to pass None to load the values from disk instead.

        Args:
            data (c4d.BaseContainer | None): The value container to load the values from or None
                when the values shall be loaded from disk.

        Returns:
            bool: True if the values were loaded successfully, False otherwise.
        """
        # @CustomSerialization: When no data is passed, we try to load the values from disk. Must be
        # removed when you do not need @CustomSerialization.
        if data is None:
            return self.LoadValuesFromDisk()

        # Check that our container has roughly the expected structure. I.e., is a BaseContainer
        # with exactly five elements. We could also check that is has exactly values at the IDs
        # we use, but I did not do that here. Note that when your plugin has multiple versions, 
        # e.g., MyPlugin v1.0 and MyPlugin v2.0, and the user has saved a layout with v1.0, and 
        # then installs v2.0, the layout data will still be legacy data. I.e., you would have to
        # handle here loading legacy data. One way to simplify this can be store a version marker
        # in the container, so that you can check more easily with which data shape you are dealing
        # with. But this is not done here, as this is a simple example.
        mxutils.CheckIterable(data, tIterable=c4d.BaseContainer, minCount=5, maxCount=5)

        # Get the weights in the container, we also do a mild sanity check. But we do not check
        # that there are exactly six elements, as Cinema 4D could add more elements in the future,
        # removing elements is very unlikely.
        weights: c4d.BaseContainer = mxutils.CheckIterable(
            data.GetContainer(self.ID_GRP_MAIN), minCount=6)

        # Set all the class fields with the values from the container. The IDs have been determined
        # by what we did in SaveValues() below.
        self._weights = weights
        self._chkPersistentValue = data.GetBool(self.ID_CHK_PERSISTENT_VALUE, False)
        self._strPersistentValue = data.GetString(self.ID_STR_PERSISTENT_VALUE, "")
        self._cmbPersistentValue = data.GetInt32(self.ID_CMB_PERSISTENT_VALUE, 0)
        self._numPersistentValue = data.GetInt32(self.ID_NUM_PERSISTENT_VALUE, 0)

        return True
    
    def LoadValuesFromDisk(self) -> bool:
        """Loads the persistent values of the dialog from disk.

        @CustomSerialization:
            This method is only needed when we want to manually save layout data to disk. You can
            remove this method when you do not need @CustomSerialization.

        Returns:
            bool: True if the values were loaded successfully, False otherwise.
        """
        # File operations should only be done from the main thread and it is a good habit to 
        # verbosely check for that instead of relying on 'being on the main thread anyway'.
        if not c4d.threading.GeIsMainThread():
            return False
        
        # Get the save path where this dialog would store its persistent values. #GetSavePath()
        # is a custom class method of the PersistentGuiCommand we implement below.
        path: str = PersistentGuiCommand.GetSavePath(self.__class__)
        fileExists: bool = os.path.exists(path)

        # Attempt to read serialized data from disk.
        if fileExists:
            hf: c4d.storage.HyperFile = c4d.storage.HyperFile()
            # A HypeFiles requires an ID to be read and written, we use here the ID of the plugin 
            # that implements this dialog, but could also use any other number, to for example 
            # distinguish between different storage format versions.
            if hf.Open(PersistentGuiCommand.ID_PLUGIN, path, c4d.FILEOPEN_READ, c4d.FILEDIALOG_NONE):
                # We serialized everything as one container, so we can just call ReadContainer() and
                # then LoadValues() with the returned container.
                data: c4d.BaseContainer | None = hf.ReadContainer()
                print(f"{data = }")
                hf.Close()  # VERY IMPORTANT: Close the hyper file when we are done with it.
                if data:
                    return self.LoadValues(data)
                

        # When reach this point and there is a file, this means that reading must have failed.
        if fileExists:
            print(f"Warning: The serialization file '{path}' exists, but failed to load. "
                   "Falling back to hardcoded default values.")
        
        # Set the default values, this will happen when the dialog has never been opened before and
        # is not part of a layout; or when we failed to read the values from disk.
        self._weights = c4d.BaseContainer(self.ID_GRP_MAIN)

        # Here we initialize the weights of the main group. The weights are stored in a BaseContainer
        # and are used to store the relative or absolute pixel values of the groups in the main group.

        # Set the number of columns and rows in the main group.
        self._weights.SetInt32(c4d.GROUPWEIGHTS_PERCENT_W_CNT, 2) # Two columns.
        self._weights.SetInt32(c4d.GROUPWEIGHTS_PERCENT_H_CNT, 2) # Two rows.

        # Set the weights for the rows and columns. Negative values are interpreted as absolute 
        # pixel values, positive values are interpreted as relative values. I.e., having three rows
        # and setting (-100, 0.5, 0.5) will set the first row to 100 pixels, and the second and third
        # row to 50% of the remaining space in the dialog. 
        #
        # For relative values we can make them sum up to 1.0, e.g., (0.5, 0.5), but that is not 
        # absolutely necessary, as the dialog will automatically set the values in relation, 
        # i.e., setting (42.0, 42.0) or (3.14159, 3.14159) will have the same effect as (0.5, 0.5).

        # Set the first column to a fixed width of 300 pixels, and the second column to a relative
        # value of whatever is left in the dialog.
        self._weights.SetFloat(c4d.GROUPWEIGHTS_PERCENT_W_VAL + 0, -300.0) # Absolute pixel value.
        self._weights.SetFloat(c4d.GROUPWEIGHTS_PERCENT_W_VAL + 1, 1.0)    # Relative value.

        # Set the first row to 30% and the second row to 70%.
        self._weights.SetFloat(c4d.GROUPWEIGHTS_PERCENT_H_VAL + 0, 0.3) # Relative value.
        self._weights.SetFloat(c4d.GROUPWEIGHTS_PERCENT_H_VAL + 1, 0.7) # Relative value.

        # Note that all these weights can be overridden by gadgets which require more space in their
        # column/row than assigned by the weights. For example, when you put an extra wide combo box
        # into a column, and then set the column width to 5px. This will not be respected, as the
        # combo box needs more space than that, the column will scale to the minimum width of the
        # combo box.

        # Set the default values for the persistent values of the dialog.
        self._chkPersistentValue = True  # The checkbox is checked by default.
        self._strPersistentValue = "Hello World!"  # The default string.
        self._cmbPersistentValue = self.ID_COLOR_GREEN  # The default combo box value.
        self._numPersistentValue = 42  # The default integer value.
        
    def SaveValues(self, data: c4d.BaseContainer | None) -> bool:
        """Saves the current values of the dialog into a BaseContainer.

        A similar method is advisable for all persistent dialogs implementations. We have implemented
        this method in a special way, as that it does not only take a BaseContainer as an argument, 
        but also allows us to pass None to save all current values to disk instead.

        Args:
            data (c4d.BaseContainer | None): The container to save the values into or None when the
                values shall be saved to disk instead.
        
        Returns:
            bool: True if the values were saved successfully, False otherwise.
        """
        # @CustomSerialization: When no data is passed, we try to save the values to disk. Must be
        # removed when you do not need @CustomSerialization.
        if data is None:
            return self.SaveValuesToDisk()
        
        # Store the weights of the main group in the container. #GroupWeightsSave() is a method
        # of GeDialog that returns the current weights for the requested group.
        weights: c4d.BaseContainer | None = self.GroupWeightsSave(self.ID_GRP_MAIN)

        # Store our data in the passed container. We store our weights and the persistent values.
        # Under which IDs we store things is up to us, we just reuse here some of the gadget IDs.
        mxutils.CheckType(data, c4d.BaseContainer)
        data.SetContainer(self.ID_GRP_MAIN, weights or c4d.BaseContainer())
        data.SetBool(self.ID_CHK_PERSISTENT_VALUE, self.GetBool(self.ID_CHK_PERSISTENT_VALUE))
        data.SetString(self.ID_STR_PERSISTENT_VALUE, self.GetString(self.ID_STR_PERSISTENT_VALUE))
        data.SetInt32(self.ID_CMB_PERSISTENT_VALUE, self.GetInt32(self.ID_CMB_PERSISTENT_VALUE))
        data.SetInt32(self.ID_NUM_PERSISTENT_VALUE, self.GetInt32(self.ID_NUM_PERSISTENT_VALUE))

        # Return the container with the values.
        return True
    
    def SaveValuesToDisk(self) -> bool:
        """Saves the persistent values of the dialog to disk.

        @CustomSerialization:
            This method is only needed when we want to manually save layout data to disk. You can   
            remove this method when you do not need @CustomSerialization.

        Returns:
            bool: True if the values were saved successfully, False otherwise.
        """
        # File operations should only be done from the main thread and it is a good habit to 
        # verbosely check for that instead of relying on 'being on the main thread anyway'.
        if not c4d.threading.GeIsMainThread():
            return False
        
        # Get the save path where this dialog would store its persistent values. #GetSavePath()
        # is a custom class method of the PersistentGuiCommand we implement below.
        path: str = PersistentGuiCommand.GetSavePath(self.__class__)

        # Create a container to store the values in. We could also write the values directly into
        # the hyper file, but since we already have #SaveValues() implemented, it is easier to just
        # write everything as a container.
        data: c4d.BaseContainer = c4d.BaseContainer()
        if not self.SaveValues(data):
            print(f"Warning: Failed to save the persistent values of {self} to a container.")
            return False
        
        # Create a HyperFile to write the values to disk. HypeFiles require an ID to be read and
        # written, we use here the ID of the plugin that implements this dialog, but could also
        # use any other number, to for example distinguish between different storage format versions.
        hf: c4d.storage.HyperFile = c4d.storage.HyperFile()
        if not hf.Open(PersistentGuiCommand.ID_PLUGIN, path, c4d.FILEOPEN_WRITE, c4d.FILEDIALOG_NONE):
            print(f"Warning: Failed to open the HyperFile '{path}' for writing.")
            return False
        
        # HyperFile is a very on the nose serialization format, as we simply write values in a 
        # sequential order when serializing data, to  read them back in the same order when
        # deserializing data. Unlike for XML or JSON, or many other places in Cinema 4D, there are 
        # no tags, key, or other identifiers that would allow us to read or write to a specific 
        # element/slot.

        # Write the first item in the file, an element of type #BaseContainer, i.e., we just write
        # everything in one go. Writing things can fail, the return value will then be False.
        res: bool = hf.WriteContainer(data)
        if not res:
            print(f"Warning: Failed to write the persistent values of {self} to HyperFile.")
        
        # IMPORTANT: Error or not, we must close the HyperFile, as we will otherwise lock the file
        # indefinitely (and also crated a memory leak).
        hf.Close()
        return res
    
    def SetWeightLabels(self) -> None:
        """Sets the labels display the group weights in the dialog.
        """
        # What is a bit counterintuitive is that weight values which have been read with GeDialog.
        # GroupWeightsSave() are often not the same values we have manually initialized them as.
        # Cinema 4D will always communicate the weights as integer pixel values, even when we set 
        # them as floating point percentage values. When we need percentage values, we must convert 
        # them back ourselves.

        # Get the row and column count in the weight container. We do not really need these values 
        # in this example. In production code these values can be used to abstractly iterate over
        # the weights, i.e., you do not have to hardcode the column and row indices as we do here.
        columnCount: int = self._weights.GetInt32(c4d.GROUPWEIGHTS_PERCENT_W_CNT)
        rowCount: int = self._weights.GetInt32(c4d.GROUPWEIGHTS_PERCENT_H_CNT)

        # Get the weights as absolute positive pixel values. Even though Cinema 4D will have converted 
        # these values to absolute pixel values, it will still return them as negative values 
        # where we set them as absolute pixel values. We would technically only need an #abs() call
        # col0, as that is the only weight which we have set as a negative absolute pixel value, 
        # casting the values from float to int is more declarative than functional, we just do this
        # to clarify the nature of the values we are working with.
        col0: int = abs(int(self._weights.GetFloat(c4d.GROUPWEIGHTS_PERCENT_W_VAL + 0))) # first column
        col1: int = abs(int(self._weights.GetFloat(c4d.GROUPWEIGHTS_PERCENT_W_VAL + 1))) # second column
        row0: int = abs(int(self._weights.GetFloat(c4d.GROUPWEIGHTS_PERCENT_H_VAL + 0))) # first row
        row1: int = abs(int(self._weights.GetFloat(c4d.GROUPWEIGHTS_PERCENT_H_VAL + 1))) # second row

        # Make all the values relative to each other again, i.e., turn them into percentages. When
        # we had more than two columns or rows, we would have to sum up all the values and then
        # divide each value by the sum of all values.
        relCol0: float = col0 / (col0 + col1) if (col0 + col1) != 0 else 0.0
        relCol1: float = col1 / (col0 + col1) if (col0 + col1) != 0 else 0.0
        relRow0: float = row0 / (row0 + row1) if (row0 + row1) != 0 else 0.0
        relRow1: float = row1 / (row0 + row1) if (row0 + row1) != 0 else 0.0

        # Set the labels.
        self.SetString(self.ID_LBL_WEIGHT_A, f"{relCol0:.2f}%")
        self.SetString(self.ID_LBL_WEIGHT_B, f"{relCol1:.2f}%")
        self.SetString(self.ID_LBL_WEIGHT_C, f"{relRow0:.2f}%")
        self.SetString(self.ID_LBL_WEIGHT_D, f"{relRow1:.2f}%")


class PersistentGuiCommand (c4d.plugins.CommandData):
    """Realizes the common implementation for a command that opens a foldable dialog.

    It effectively realizes the button to be found in menus, palettes, and the command manager 
    that opens our dialog. Technically, this is the concrete plugin we implement. But it here
    only plays a secondary role to the dialog, where all the logic is implemented.
    """
    # The dialog hosted by the plugin.
    REF_DIALOG: PersistentGuiDialog | None = None

    @property
    def Dialog(self) -> PersistentGuiDialog:
        """Returns the class bound dialog instance.
        """
        if self.REF_DIALOG is None:
            self.REF_DIALOG = PersistentGuiDialog()

        return self.REF_DIALOG

    def Execute(self, doc: c4d.documents.BaseDocument) -> bool:
        """Folds or unfolds the dialog.
        """
        # Fold the dialog, i.e., hide it if it is open and unfolded.
        if self.Dialog.IsOpen() and not self.Dialog.GetFolding():
            self.Dialog.SetFolding(True)
        # Open or unfold the dialog. When we open the dialog, we do it asynchronously, i.e., the
        # user can unfocus the dialog and continue working in Cinema 4D, while the dialog is open.
        # The alternative would be to open a modal dialog, which would force the user to focus the
        # dialog until it is closed. Modal can be useful but cannot be docked in the layout.
        else:
            self.Dialog.Open(c4d.DLG_TYPE_ASYNC, self.ID_PLUGIN, defaultw=500, defaulth=300)

        return True

    def RestoreLayout(self, secret: any) -> bool:
        """Restores the dialog on layout changes.

        Implementing this is absolutely necessary, as otherwise the dialog will not be
        restored when the user changes the layout of Cinema 4D.
        """
        return self.Dialog.Restore(self.ID_PLUGIN, secret)

    def GetState(self, doc: c4d.documents.BaseDocument) -> int:
        """Sets the command icon state of the plugin.

        With this you can tint the command icon blue when the dialog is open or grey it out when
        some condition is not met (not done here). You could for example disable the plugin when
        there is nothing selected in a scene, when document is not in polygon editing mode, etc.
        """
        # The icon is never greyed out, the button can always be clicked.
        result: int = c4d.CMD_ENABLED

        # Tint the icon blue when the dialog is already open.
        if self.Dialog.IsOpen() and not self.Dialog.GetFolding():
            result |= c4d.CMD_VALUE

        return result
    
    # --- Custom methods and attributes ------------------------------------------------------------
    
    # The unique ID of the plugin, it must be obtained from developers.maxon.net.
    ID_PLUGIN: int = 10656351

    # The name and help text of the plugin.
    STR_NAME: str = "Py - Persistent Gui"
    STR_HELP: str = "Opens a dialog that persistently stores group weights and values."

    # A lookup table for the save paths for classes used by this plugin, so that we do not have to
    # establish them each time we are being asked for a save path.
    DICT_SAVE_PATHS: dict[str, str] = {}

    @classmethod
    def Register(cls: typing.Type, iconId: int) -> None:
        """Registers the command plugin.

        This is a custom method and not part of the CommandData interface.
        """
        # Load one of the builtin icons of Cinema 4D as the icon of the plugin, you can browse the
        # builtin icons under:
        #
        #   https://developers.maxon.net/docs/py/2023_2/modules/c4d.bitmaps/RESOURCEIMAGE.html
        #
        # You could also load your own icon file here.
        bitmap: c4d.bitmaps.BaseBitmap = c4d.bitmaps.InitResourceBitmap(iconId)

        # The instance of the command that will is registered and will live throughout the whole
        # lifetime of the Cinema 4D session. I.e., commands are effectively singletons (although
        # not formally implemented as such).
        command: object = cls()

        # Register the command, a registration can fail, for example when the ID is already taken.
        # But if this happens, Cinema 4D will print an error message to the console on its own. When
        # we register multiple plugins, it can make sense to stop registering plugins, when one of
        # them fails. But we do not need this here, so we just ignore the return value of the
        # RegisterCommandPlugin() function.
        c4d.plugins.RegisterCommandPlugin(
            id=cls.ID_PLUGIN, str=cls.STR_NAME, info=0, icon=bitmap, help=cls.STR_HELP, dat=command)
        
    @classmethod
    def GetSavePath(cls: typing.Type, entity: typing.Type) -> str:
        """Returns a save path for the given entity in the instance bound user preferences directory
        of this plugin.

        This method provides a pattern for how obtain and manage save paths for entities in a plugin
        (suite). This mostly has been written with a plugin in mind that has to save multiple files,
        for a singular file case one can also do with less abstraction, but it also does not hurt to
        use this template. 
        
        The example saves to maxon.APPLICATION_URLTYPE.PREFS_DIR, i.e., preferences directory which
        is bound to the running instance of Cinema 4D. We could also save to .GLOBALPREFS_DIR, which
        as its name suggests, can be seen by all Cinema 4D installations on the system, but would 
        then also have to handle possible plugin version conflicts.

        This is a custom method and not part of the CommandData interface.

        Args:
            entity (typing.Type): The class to get the save path for. Will derive the path from the
                class name.
        """
        # Check if the entity is a class, i.e., that it has a valid __name__ attribute.
        name: str = getattr(entity, "__name__", "")
        if name == "":
            raise ValueError(f"The entity must have a non empty __name__ attribute. Got: {entity}.")
        
        # Check if we have already established a save path for this entity.
        if name in cls.DICT_SAVE_PATHS:
            return cls.DICT_SAVE_PATHS[name]
        
        # Define the save path. We could save content to the plugin directory, but that is not
        # recommended, as the user might not have write permissions there. The better place to save
        # content is the user preferences directory, which is guaranteed to be writable. We place
        # all content in a subdirectory named after the plugin (cls.__name__) of the `prefs/plugins` 
        # directory. We could also save directly to `prefs/plugins/`, but when a plugin has multiple
        # files, it is better to have a subdirectory for the plugin.
        pref: maxon.Url = maxon.Application.GetUrl(maxon.APPLICATION_URLTYPE.PREFS_DIR)
        sysPath: str = pref.GetSystemPath()
        pluginPref: str = os.path.join(sysPath, "plugins", str(cls.__name__))

        # There is no guarantee that the plugins subdirectory exists, so we have to create it.
        if not os.path.exists(pluginPref):
            try:
                os.makedirs(pluginPref, exist_ok=True)
            except OSError as e:
                raise OSError(f"Failed to create the directory {pluginPref}.") from e
            
        # Define the final hyper file path for the given #entity class, store the path in the
        # lookup table, so that we do not have to establish it again, and return it. E.g., the
        # final path could be for example:
        #
        #   ./{c4d_version}/plugins/PersistentGuiCommand/someEntity.hf
        #
        fPath: str = os.path.join(pluginPref, f"{name}.hf")
        cls.DICT_SAVE_PATHS[name] = fPath

        return fPath


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == '__main__':
    PersistentGuiCommand.Register(iconId=465001193)
