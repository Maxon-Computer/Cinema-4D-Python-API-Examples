"""Initializes a bitmap from a vector image file.

You can run this example by executing it in the Script Manager of Cinema 4D. It searches the
Cinema 4D installation for an SVG file, rasterizes it at several sizes, and displays the results.

Topics:
    * Rasterizing vector images (SVG) into bitmaps
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0.0"

import os
import typing

import c4d
import maxon


def IterSvgFiles(path: str, count: int) -> typing.Iterator[str]:
    """Yields the first `count` SVG files found in the given path and its subdirectories.
    """
    if path.startswith("file:///"):
        path = path[8:]  # Remove the "file:///" prefix

    for root, _, files in os.walk(path):
        for name in files:
            if name.lower().endswith(".svg"):
                yield os.path.join(root, name)
                count -= 1
                if count == 0:
                    return

def main() -> None:
    """Finds an SVG file in the Cinema 4D installation and displays rasterized versions of it.
    """
    # Find the first three SVG files in the Cinema 4D installation directory.
    searchPath: str = str(maxon.Application.GetUrl(maxon.APPLICATION_URLTYPE.STARTUP_DIR))
    for svgPath in IterSvgFiles(searchPath, 3):
        name: str = os.path.basename(svgPath)

        # For each SVG file, rasterize it at several sizes and display the resulting bitmaps.
        for prefHeight in (32, 128, 512):
            bitmap: c4d.bitmaps.BaseBitmap = c4d.bitmaps.BaseBitmap()
            if bitmap.InitWithVectorFile(svgPath, prefHeight) != c4d.IMAGERESULT_OK:
                print(f"Failed to rasterize SVG file: {svgPath}")
                continue

            # Remember that you have enable transparencies via View > Enable Transparency in the 
            # the Picture Viewer to see the transparent background of the rasterized SVG.
            c4d.bitmaps.ShowBitmap(bitmap, f"{name}_{prefHeight if prefHeight > 0 else 'original'}")

if __name__ == "__main__":
    main()
