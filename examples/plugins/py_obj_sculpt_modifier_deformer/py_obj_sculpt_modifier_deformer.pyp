"""Demonstrates how to implement a modifier object that modifies a point object using the pull sculpting brush tool.

The modifier applies the pull sculpting brush behavior to a point object and illustrates the ObjectData callbacks needed to modify generated geometry.

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:
    - Implementing a modifier ObjectData plugin
    - Applying sculpt brush behavior to point geometry
"""
__copyright__ = "Copyright 2026, MAXON Computer"
__author__ = "Kent Barber"
__date__ = "25/08/2026"
__license__ = "Apache-2.0 license"
__version__ = "16.0.0"

import c4d
import random

# be sure to use a unique ID obtained from developers.maxon.net
PLUGIN_ID = 1031586
ID_SCULPT_BRUSH_PULL_MODIFIER = 1030505


class SculptModifierDeformer(c4d.plugins.ObjectData):

    def __init__(self):
        self.brushInterface = None

    def Init(self, node, isCloneInit=False):
        """Called when Cinema 4D Initialize the ObjectData (used to define, default values).

        Args:
            node (c4d.GeListNode): The instance of the ObjectData.
            isCloneInit (bool): True if the object data is a copy of another one.

        Returns:
            True on success, otherwise False.
        """
        self.InitAttr(node, float, c4d.PYSCULPTMODIFIERDEFORMER_RADIUS)
        self.InitAttr(node, float, c4d.PYSCULPTMODIFIERDEFORMER_PRESSURE)
        self.InitAttr(node, bool, c4d.PYSCULPTMODIFIERDEFORMER_STAMP_ACTIVE)
        self.InitAttr(node, int, c4d.PYSCULPTMODIFIERDEFORMER_NUMSTAMPS)
        self.InitAttr(node, bool, c4d.PYSCULPTMODIFIERDEFORMER_STAMP_USEFALLOFF)
        self.InitAttr(node, int, c4d.PYSCULPTMODIFIERDEFORMER_SEED)
        self.InitAttr(node, float, c4d.PYSCULPTMODIFIERDEFORMER_STAMP_ROTATION)

        if not isCloneInit:
            node[c4d.PYSCULPTMODIFIERDEFORMER_RADIUS] = 20
            node[c4d.PYSCULPTMODIFIERDEFORMER_PRESSURE] = 0.2
            node[c4d.PYSCULPTMODIFIERDEFORMER_STAMP_ACTIVE] = False
            node[c4d.PYSCULPTMODIFIERDEFORMER_NUMSTAMPS] = 10
            node[c4d.PYSCULPTMODIFIERDEFORMER_STAMP_USEFALLOFF] = True
            node[c4d.PYSCULPTMODIFIERDEFORMER_SEED] = 0
            node[c4d.PYSCULPTMODIFIERDEFORMER_STAMP_ROTATION] = 0

        self.brushInterface = c4d.modules.sculpting.SculptModifierInterface()

        return True

    def Message(self, node, msgId, data):
        """Called by Cinema 4D part to notify the object to a special event.

        Args:
            node (c4d.BaseObject): The instance of the ObjectData.
            msgId (int): The message ID type.
            data (Any): The message data, the type depends on the message passed.

        Returns:
            bool: Depends of the message type, most of the time True.
        """
        # MSG_MENUPREPARE is received when called from the menu, to let some setup work.
        # In the case of this message, the data passed is the BaseDocument the object is inserted
        if msgId == c4d.MSG_MENUPREPARE:
            # Enables the modifier
            node.SetDeformMode(True)
        return True

    def ModifyObject(self, mod, doc, op, op_mg, mod_mg, lod, flags, thread):
        """Called by Cinema 4D with the object to modify.

        Args:
            mod (c4d.BaseObject): The Python Modifier.
            doc (c4d.documents.BaseDocument): The document containing the plugin object.
            op (c4d.BaseObject): The object to modify.
            op_mg (c4d.Matrix): The object's world matrix.
            mod_mg (c4d.Matrix): The modifier object's world matrix.
            lod (float): The level of detail.
            flags (int): Currently unused.
            thread (c4d.threading.BaseThread): The calling thread.

        Returns:
            bool: True if the object was modified, otherwise False.
        """
        # Retrieves object parameters values
        data = mod.GetDataInstance()
        radius = data[c4d.PYSCULPTMODIFIERDEFORMER_RADIUS]
        pressure = data[c4d.PYSCULPTMODIFIERDEFORMER_PRESSURE] * 100.0
        stampActive = data[c4d.PYSCULPTMODIFIERDEFORMER_STAMP_ACTIVE]
        stampTexture = data[c4d.PYSCULPTMODIFIERDEFORMER_STAMP_TEXTURE]
        numStamps = data[c4d.PYSCULPTMODIFIERDEFORMER_NUMSTAMPS]
        useFalloff = data[c4d.PYSCULPTMODIFIERDEFORMER_STAMP_USEFALLOFF]
        seed = data[c4d.PYSCULPTMODIFIERDEFORMER_SEED]
        rotation = data[c4d.PYSCULPTMODIFIERDEFORMER_STAMP_ROTATION]

        # Checks if the passed object is not a polygon object (so its only modify polygon object)
        if not op.IsInstanceOf(c4d.Opolygon):
            return True

        # Initializes the brushInterface with the Polygon object passed
        if not self.brushInterface.Init(op):
            return True

        # Retrieves the settings for the brush
        brushData = self.brushInterface.GetDefaultData()

        # Defines settings according our needs
        modifierData = c4d.BaseContainer()
        brushData.SetFloat(c4d.MDATA_SCULPTBRUSH_SETTINGS_STRENGTH, pressure)
        brushData.SetFloat(c4d.MDATA_SCULPTBRUSH_SETTINGS_RADIUS, radius)
        brushData.SetBool(c4d.MDATA_SCULPTBRUSH_STAMP, stampActive)
        brushData.SetFilename(c4d.MDATA_SCULPTBRUSH_STAMP_TEXTUREFILENAME, stampTexture)
        brushData.SetBool(c4d.MDATA_SCULPTBRUSH_STAMP_USEFALLOFF, useFalloff)
        brushData.SetFloat(c4d.MDATA_SCULPTBRUSH_STAMP_ROTATION_VALUE, rotation)

        # Push back our settings to the brush
        self.brushInterface.SetData(brushData, modifierData)

        # Defines the random seed, so random is consistent over time
        random.seed(seed)

        for i in range(numStamps):
            # Retrieves a random a pointIndex
            ptId = int(random.random() * op.GetPointCount())

            # Applies the modification (like if the user click use the brush tool),
            # this will modify the object brushInterface is initialized with.
            self.brushInterface.ApplyModifier(
                ID_SCULPT_BRUSH_PULL_MODIFIER, ptId, brushData, modifierData)

        # Notifies the object, that internal data changed and it needs to be updated
        op.Message(c4d.MSG_UPDATE)

        return True


if __name__ == "__main__":
    # Registers the object plugin. PLUGINFLAG_HIDEPLUGINMENU hides the natural menu entry of this
    # plugin. Omit this flag or replace it by 0 when you do not have custom menu handling as the SDK 
    # has (see py_menu).
    c4d.plugins.RegisterObjectPlugin(id=PLUGIN_ID,
                                     str="Py SDK - Sculpt Modifier Deformer",
                                     g=SculptModifierDeformer,
                                     description="opysculptmodifierdeformer",
                                     icon=None,
                                     info=c4d.OBJECT_MODIFIER | c4d.PLUGINFLAG_HIDEPLUGINMENU)
