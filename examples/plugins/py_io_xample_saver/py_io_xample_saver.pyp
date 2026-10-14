"""Demonstrates how to implement a custom bitmap saver to export a custom picture format into Cinema 4D.

The BitmapSaverData plugin exports a custom picture format from Cinema 4D. It is paired with the corresponding bitmap loader example.

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:
    - Writing a custom bitmap format
    - Exporting image data with BitmapSaverData
"""
__copyright__ = "Copyright 2026, MAXON Computer"
__author__ = "Maxime Adam"
__date__ = "25/08/2026"
__license__ = "Apache-2.0 license"
__version__ = "23.0.0"

import c4d
import struct
import bz2


# Be sure to use a unique ID obtained from developers.maxon.net
PLUGIN_ID = 1025254

BMP_NAME = "Py SDK - XAMPLE Saver"

BMP_IDENTIFIER = b"XAMPLE"
BMP_SUFFIX = "xample"


class MyXampleSaver(c4d.plugins.BitmapSaverData):
    """Data class to export a *.xample file"""

    COMPRESSION = 1000
    STANDARD_COMP = 9

    def Edit(self, data):
        """Called by Cinema 4D, to query the option for the exporter.

        Args:
            data (c4d.BaseContainer): The settings for the plugin.

        Returns:
            True if the dialog opened successfully
        """
        std = data.GetInt32(self.COMPRESSION, self.STANDARD_COMP)

        # Asks for Compression values
        while True:
            # Opens a popup dialog to ask for the compression value
            result = c4d.gui.InputDialog(title="Compression", preset=std)
            # If nothing, or user cancel, simply leave
            if result is None:
                return True

            # Try to convert the entered value in integer otherwise ask again.
            try:
                result = int(result)
            except ValueError as e:
                c4d.gui.MessageDialog(str(e), c4d.GEMB_OK)
                continue

            # Checks if entered value is between 1, and 9, otherwise ask again.
            if not 1 <= result <= 9:
                c4d.gui.MessageDialog("Value '%i' must be between 1 and 9." % result, c4d.GEMB_OK)
                continue

            # Defines the compress depth in the BaseContainer
            data.SetInt32(self.COMPRESSION, result)
            return True

    def Save(self, fn, bm, data, savebits):
        """Called by Cinema 4D, when the plugin should save BaseBitmap as a files.

        Args:
            fn (str): The name of the file.
            bm (c4d.bitmaps.BaseBitmap): The Bitmap, to be filled with the data (need to be initialized).
            data (c4d.BaseContainer): The settings for the plugin.
            savebits (SAVEBIT): Flags defines for the save process.

        Returns:
            IMAGERESULT
        """
        # Opens the file in binary write mode
        with open(fn, "wb") as fn:
            # Writes file identifier
            fn.write(BMP_IDENTIFIER)

            # Writes bit depth, width and height information
            p = struct.pack("iii", bm.GetBt(), bm.GetBw(), bm.GetBh())
            fn.write(p)

            # Retrieves bitmap data, in python 2.7 str and bits are the same, so we
            # are storing raw bits here
            content = b""
            # Iterates each lines to fill the BaseBitmap
            for y in range(bm.GetBh()):
                # Iterates each rows to fill the BaseBitmap
                for x in range(bm.GetBw()):

                    # Extracts red, green, blue information
                    r, g, b = bm[x, y]

                    # Stores pixel information as bits
                    content += struct.pack("hhh", r, g, b)

            # Compress pixels information
            compression = data.GetInt32(self.COMPRESSION, self.STANDARD_COMP)

            # Writes the compressed data into the file
            fn.write(bz2.compress(content, compression))

        return c4d.IMAGERESULT_OK


if __name__ == "__main__":
    # Registers the bitmap saver plugin
    c4d.plugins.RegisterBitmapSaverPlugin(id=PLUGIN_ID,
                                          str=BMP_NAME,
                                          info=c4d.PLUGINFLAG_BITMAPSAVER_ALLOWOPTIONS |
                                          c4d.PLUGINFLAG_BITMAPSAVER_SUPPORT_8BIT |
                                          c4d.PLUGINFLAG_BITMAPSAVER_FORCESUFFIX,
                                          dat=MyXampleSaver(),
                                          suffix=BMP_SUFFIX)
