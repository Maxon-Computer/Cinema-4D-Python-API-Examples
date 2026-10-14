"""Demonstrates how to implement a custom bitmap loader to import a custom picture format into Cinema 4D.

The BitmapLoaderData plugin recognizes a custom picture format and imports it into Cinema 4D. It is paired with the corresponding bitmap saver example.

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:
    - Recognizing a custom bitmap format
    - Loading image data with BitmapLoaderData
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
PLUGIN_ID = 1025255

BMP_NAME = "Py SDK - XAMPLE Loader"

BMP_IDENTIFIER = b"XAMPLE"


class MyXampleLoader(c4d.plugins.BitmapLoaderData):
    """Data class to import a *.xample file"""

    def Identify(self, name, probe, size):
        """Called by Cinema 4D, to identifie your file type (know if this Bitmap Loader can be used with the current Bitmap).

        Args:
            name (str): The name of the file.
            probe (buffer): The start of data from the file currently tested.
            size (int): The size of the probe for testing this file type.

        Returns:
            True if the plugin can load this file.
        """
        # Checks if image starts with identifier flag
        return probe[:len(BMP_IDENTIFIER)] == BMP_IDENTIFIER

    def Load(self, name, bm, frame):
        """Called by Cinema 4D, when the plugin should loads the files as a BaseBitmap.

        Args:
            name (str): The name of the file.
            bm (c4d.bitmaps.BaseBitmap): The Bitmap, to be filled with the data (need to be initialized).
            frame (int): The current frame number for file format containing picture sequence (Quicktime, AVI...)

        Returns:
            IMAGERESULT
        """
        # Opens the file in binary read mode
        with open(name, "rb") as fn:
            # Skips identifier
            lines = fn.read()[len(BMP_IDENTIFIER):]

            # Calculates the bits size of 3 int and 3 char
            intBitsSize = struct.calcsize("iii")
            chatBitsSize = struct.calcsize("hhh")

            # Extracts bit depth, width and height information
            bt, width, height = struct.unpack("iii", lines[:intBitsSize])

            # Initialize the bitmap with the information provided
            if bm.Init(width, height, bt) != c4d.IMAGERESULT_OK:
                raise MemoryError("Failed to initialize the BaseBitmap.")

            # Removes the offset so we can start with position 0 of the pixel information
            lines = lines[intBitsSize:]

            # Decompress to raw data
            lines = bz2.decompress(lines)

            # Iterates each lines to fill the BaseBitmap
            for x in range(width):
                # Iterates each row
                for y in range(height):
                    # Retrieves memory position according current x and y pixels
                    fr = (y * width * chatBitsSize) + (x * chatBitsSize)

                    # Extracts red, green, blue information
                    r, g, b = struct.unpack("hhh", lines[fr:fr + chatBitsSize])

                    # Assigns pixel value for x, y pixel
                    bm[x, y] = r, g, b

        return c4d.IMAGERESULT_OK


if __name__ == "__main__":
    # Registers the bitmap loader plugin
    c4d.plugins.RegisterBitmapLoaderPlugin(id=PLUGIN_ID,
                                           str=BMP_NAME,
                                           info=0,
                                           dat=MyXampleLoader())
