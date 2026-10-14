"""Demonstrates the usage of the central bitmap type.

Run this example in the Cinema 4D Script Manager.

Topics:
    - Copying containers
    - Iterating over containers
    - Nested containers
    - Container IDs
    - Using containers in message and callback contexts
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027"

import c4d
import os
import maxon

doc: c4d.documents.BaseDocument # The active document.

def FindSvgFile() -> str:
    """Returns the first SVG file path found in the Cinema 4D installation directory.
    """
    path: str = str(maxon.Application.GetUrl(maxon.APPLICATION_URLTYPE.STARTUP_DIR))
    if path.startswith("file:///"):
        path = path[8:]  # Remove a "file:///" prefix, as Python cannot handle it in os.walk.

    for root, _, files in os.walk(path):
        for name in files:
            if name.lower().endswith(".svg"):
                return os.path.join(root, name)
    return ""

SVG_PATH: str = FindSvgFile()
if not SVG_PATH:
    raise FileNotFoundError("No SVG file found in the Cinema 4D installation directory.")


def main() -> None:
    """Finds an SVG file in the Cinema 4D installation and displays rasterized versions of it.
    """
    print("\n--- Instantiation -----------------------------------------------------------------\n")

    # BaseBitmap is the central bitmap type in the Cinema API.

    # Initialize an empty bitmap from scratch. Bitmaps are one of the cases where we do not really
    # have to shield us against allocation failures with mxutils.CheckType on __init__() because
    # the actual allocation happens in Init() rather than in __init__().
    bmp: c4d.bitmaps.BaseBitmap = c4d.bitmaps.BaseBitmap()
    if bmp.Init(x=512, y=512, depth=32, flags=c4d.INITBITMAPFLAGS_NONE) != c4d.IMAGERESULT_OK:
        raise RuntimeError("Failed to initialize bitmap")

    # Bitmaps can be displayed with c4d.bitmaps.ShowBitmap().
    c4d.bitmaps.ShowBitmap(bmp, "Empty Bitmap")
    print(f"{bmp = }")

    # We can load existing bitmap files from disk using InitWith(). The URL could be a local file
    # url such as "c:/path/to/your/bitmap/file.png" or an asset URL as we use here. This will in fact
    # be able any maxon.Url scheme, i.e., also things such as ram disk, network drive, etc. URLs.
    bmp: c4d.bitmaps.BaseBitmap = c4d.bitmaps.BaseBitmap()
    bmp.InitWith("asset:///file_5b6a5fe03176444c")
    c4d.bitmaps.ShowBitmap(bmp, "UV Test Grid Asset")

    # Last but not least, you can also load vector files with InitWithVectorFile(). Svg files can
    # be initialized to a 'preferred height' for rasterization. Remember that you have to enable 
    # transparencies via View > Enable Transparency in the Picture Viewer to see transparencies.
    for prefHeight in (32, 128, 512):
        bmp: c4d.bitmaps.BaseBitmap = c4d.bitmaps.BaseBitmap()
        if bmp.InitWithVectorFile(SVG_PATH, prefHeight) != c4d.IMAGERESULT_OK:
            print(f"Failed to rasterize SVG file: {SVG_PATH}")
            continue

        name: str = os.path.basename(SVG_PATH)
        c4d.bitmaps.ShowBitmap(bmp, f"{name}-{prefHeight}")

    print("\n--- Reading Basic Data ------------------------------------------------------------\n")

    # Load the UV Test Grid asset again.
    bmp: c4d.bitmaps.BaseBitmap = c4d.bitmaps.BaseBitmap()
    bmp.InitWith("asset:///file_5b6a5fe03176444c")

    # Get the width, height, bit depth, and buffer size of a line of the bitmap.
    width: int = bmp.GetBw()
    height: int = bmp.GetBh()
    depth: int = bmp.GetBt()
    lineBufferSize: int = bmp.GetBpz()
    colorMode: int = bmp.GetColorMode()

    # The number of channels.
    channels: int = bmp.GetChannelCount()
    print(f"{width = }, {height = }, {depth = }, {lineBufferSize = }, {colorMode = }, {channels = }")

    print("\n--- Getting Pixels ----------------------------------------------------------------\n")

    # Singular pixel access is rather slow and should be avoided when possible.
    firstLine: list[c4d.Vector] = [bmp.GetPixelDirect(x, 0) for x in range(width)]
    print(f"firstLine (slow access) = {firstLine}")

    # It it s much more performant to access pixels in bulk with GetPixelCnt(). This method can
    # at most address a full row of pixels at a time.
    # The increment is the number of bytes between pixels in the destination buffer. Keep the
    # bitmap's native mode to avoid an unnecessary color-depth conversion.
    increment: int = bmp.GetBt() // 8
    byteBuffer: bytearray = bytearray(width * increment)
    buffer: memoryview = memoryview(byteBuffer)
    bmp.GetPixelCnt(0, 0, width, buffer, increment, colorMode, c4d.PIXELCNT_NONE)

    firstLine: list[c4d.Vector] = [c4d.Vector(buffer[i], buffer[i + 1], buffer[i + 2]) 
                                   for i in range(0, len(buffer), 3)]

    print(f"firstLine (fast access) = {firstLine}")

    print("\n--- Setting Pixels ----------------------------------------------------------------\n")

    # Exactly the same applies to setting pixels. BaseBitmap is also not a draw interface, use
    # GeClipMap for such tasks.

    # Set the (2, 2) pixel to pure red.
    bmp.SetPixel(2, 2, 255, 0, 0)

    # With buffer access, wwe write the 4th row into black to red gradient.
    colors: list[c4d.Vector] = [c4d.utils.MixVec(c4d.Vector(0), 
                                                 c4d.Vector(1, 0, 0), 
                                                 i / width) 
                                for i in range(width)]

    byteBuffer: bytearray = bytearray(width * increment)
    buffer: memoryview = memoryview(byteBuffer)
    for x in range(width):
        offset: int = x * 3
        buffer[offset + 0] = int(colors[x].x * 255) 
        buffer[offset + 1] = int(colors[x].y * 255)
        buffer[offset + 2] = int(colors[x].z * 255)

    if not bmp.SetPixelCnt(0, 3, width, byteBuffer, increment, colorMode, c4d.PIXELCNT_NONE):
        raise RuntimeError("Failed to set pixel data")

    c4d.bitmaps.ShowBitmap(bmp, "Manipulated Bitmap")
    print("Drew red gradient on the 4th row")

    print("\n--- Copying and Cloning -----------------------------------------------------------\n")


if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
