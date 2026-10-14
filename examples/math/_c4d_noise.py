"""Demonstrates working with noise functions.

Topics:
    - Simple noise functions (Noise, Turbulence, WavyTurbulence)
    - C4DNoise class and its usage

Related:
    io/_c4d_basebitmap.py
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

def GenerateBitmap(data: list[float], width: int, height: int) -> c4d.bitmaps.BaseBitmap:
    """Generates a bitmap from an array of floats.
    """
    if width < 1 or height < 1:
        raise ValueError("Bitmap dimensions must be positive.")
    if len(data) != width * height:
        raise ValueError("Data size must match the bitmap dimensions.")

    bmp: c4d.bitmaps.BaseBitmap = c4d.bitmaps.BaseBitmap()
    if bmp.Init(width, height, c4d.COLORMODE_RGBw) != c4d.IMAGERESULT_OK:
        raise RuntimeError("Failed to initialize bitmap")

    rowBuffer: bytearray = bytearray(width * c4d.COLORBYTES_RGBf)
    byteView: memoryview = memoryview(rowBuffer)
    floatView: memoryview = byteView.cast("f")
    
    for y in range(height):
        for x in range(width):
            value: float = data[y * width + x]
            offset: int = x * 3
            floatView[offset] = value
            floatView[offset + 1] = value
            floatView[offset + 2] = value

        bmp.SetPixelCnt(0, y, width, byteView, c4d.COLORBYTES_RGBf, c4d.COLORMODE_RGBf, c4d.PIXELCNT_0)

    return bmp


def main() -> None:
    """Runs the example.
    """
    print("\n--- Simple Noises -----------------------------------------------------------------\n")
    # NOTE: Cinema uses positional arguments only. The named arguments in this example have been
    # added for clarity, but they are ignored by Cinema 4D. You must pass the arguments in the order
    # shown here.

    # The size of our noise array.
    sizeX: int = 256
    sizeY: int = 256
    scale: float = 0.01 # The 'zoom' factor for the noise functions. One unit is a relatively
                        # large distance in noise space, so if we would use raw pixel coordinates,
                        # we would not see much detail because we are zoomed out to far.

    # In c4d.utils.noise are some easy to use no-instantiation noise functions such as Noise, 
    # Turbulence, and WavyTurbulence.

    # Generate a 256x256 Noise array and display it in the Picture Viewer. p is the sample position
    # and t the sample time (for animated noise).
    data: list[float] = [
        c4d.utils.noise.Noise(p=c4d.Vector(x * scale, y * scale, 0), t=0)                        
        for y in range(sizeY)
        for x in range(sizeX)
    ]
    c4d.bitmaps.ShowBitmap(GenerateBitmap(data, sizeX, sizeY), "noise.Noise")

    # Generate a 256x256 Turbulence array and display it in the Picture Viewer. oct are the number 
    # of octaves for the turbulence.
    data = [
        c4d.utils.noise.Turbulence(p=c4d.Vector(x * scale, y * scale, 0), oct=4, abs=True, t=0)  
        for y in range(sizeY)
        for x in range(sizeX)
    ]
    c4d.bitmaps.ShowBitmap(GenerateBitmap(data, sizeX, sizeY), "noise.Turbulence")

    # Generate a 256x256 WavyTurbulence array and display it in the Picture Viewer.
    data = [
        c4d.utils.noise.WavyTurbulence(p=c4d.Vector(x * scale, y * scale, 0), t=0, oct=4, start=0.25)
        for y in range(sizeY)
        for x in range(sizeX)
    ]
    c4d.bitmaps.ShowBitmap(GenerateBitmap(data, sizeX, sizeY), "noise.WavyTurbulence")

    print("\n--- C4D Noises --------------------------------------------------------------------\n")

    # And then there is the instantiatable class c4d.utils.noise.C4DNoise, which provides access to
    # all iconic Cinema 4D noises.
    noise: c4d.utils.noise.C4DNoise = c4d.utils.noise.C4DNoise(seed=1234)
    noise.InitFbm(lMaxOctaves=8, rLacunarity=2, h=0.5)

    # Generate a 256x256 box noise array and display it in the Picture Viewer. t is the noise type, 
    # two_d indicates whether the noise is 2D or 3D, p is the sample position, time is here the
    # sample time, octaves is the number of octaves, absolute indicates whether to take the absolute
    # value of the noise, sampleRad is the sample radius, detailAtt is the detail attenuation, and
    # t_repeat is the temporal repeat. Every argument after p is optional.
    data = [
        noise.Noise(t=c4d.NOISE_BOX_NOISE, two_d=True, p=c4d.Vector(x * scale, y * scale, 0), 
                    time=0, octaves=4, absolute=False, sampleRad=0.25, detailAtt=0.25, t_repeat=0)
        for y in range(sizeY)
        for x in range(sizeX)
    ]
    c4d.bitmaps.ShowBitmap(GenerateBitmap(data, sizeX, sizeY), "C4DNoise - BoxNoise")

    # And the same for a ober noise, see the docs for all noise types.
    data = [
        noise.Noise(t=c4d.NOISE_OBER, two_d=True, p=c4d.Vector(x * scale, y * scale, 0), 
                    time=0, octaves=4, absolute=False, sampleRad=0.25, detailAtt=0.25, t_repeat=0)
        for y in range(sizeY)
        for x in range(sizeX)
    ]
    c4d.bitmaps.ShowBitmap(GenerateBitmap(data, sizeX, sizeY), "C4DNoise - Ober")


if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
