"""
Copyright: MAXON Computer GmbH
Author: Maxime Adam

Description:
    - Convert a Polygon Object to a Volume and save this volume to a VDB File
    - Save a VDB file.

Class/method highlighted:
    - maxon.Vector
    - maxon.BaseArray
    - maxon.frameworks.volume.VolumeRef
    - maxon.frameworks.volume.VolumeConversionPolygon
    - maxon.frameworks.volume.VolumeToolsInterface.MeshToVolume()
    - maxon.frameworks.volume.VolumeToolsInterface.SaveVDBFile()

Compatible:
    - Win / Mac
    - R20, R21, S22, R23
"""
import c4d
import maxon
from maxon.frameworks import volume
import os


def polygonToVolume(obj):
    # Checks if the input obj is a PolygonObject
    if not obj.IsInstanceOf(c4d.Opolygon):
        raise TypeError("obj is not a c4d.Opolygon.")

    # Retrieves the world matrices of the object
    matrix = obj.GetMg()

    # Creates a BaseArray (list) of all points position in world space
    vertices = maxon.BaseArray(maxon.Vector)
    vertices.Resize(obj.GetPointCount())
    for i, pt in enumerate(obj.GetAllPoints()):
        vertices[i] = pt * matrix

    # Sets polygons
    polygons = maxon.BaseArray(maxon.frameworks.volume.VolumeConversionPolygon)
    polygons.Resize(obj.GetPolygonCount())
    for i, poly in enumerate(obj.GetAllPolygons()):
        newPoly = maxon.frameworks.volume.VolumeConversionPolygon()
        newPoly.a = poly.a
        newPoly.b = poly.b
        newPoly.c = poly.c

        if poly.IsTriangle():
            newPoly.SetTriangle()
        else:
            newPoly.d = poly.d

        polygons[i] = newPoly

    polygonObjectMatrix = maxon.Matrix()
    polygonObjectMatrix.off = obj.GetMg().off
    polygonObjectMatrix.v1 = obj.GetMg().v1
    polygonObjectMatrix.v2 = obj.GetMg().v2
    polygonObjectMatrix.v3 = obj.GetMg().v3
    gridSize = 10
    bandWidthInterior = 1
    bandWidthExterior = 1
    thread = maxon.ThreadRef()

    # Before R21
    if c4d.GetC4DVersion() < 21000:
        volumeRef = maxon.frameworks.volume.VolumeToolsInterface.MeshToVolume(vertices,
                                                                              polygons, polygonObjectMatrix,
                                                                              gridSize,
                                                                              bandWidthInterior, bandWidthExterior,
                                                                              thread, None)
    else:
        volumeRef = maxon.frameworks.volume.VolumeToolsInterface.MeshToVolume(vertices,
                                                                              polygons, polygonObjectMatrix,
                                                                              gridSize,
                                                                              bandWidthInterior, bandWidthExterior,
                                                                              thread,
                                                                              maxon.POLYGONCONVERSIONFLAGS.NONE, None)
    
    return volumeRef


def main():
    # Gets selected objects
    objList = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0)
    if not objList:
        raise RuntimeError("Failed to retrieve selected objects")

    # Opens a LoadDialog to define the path of the VDB file to save
    filePath = c4d.storage.SaveDialog()

    # Leaves if nothing was selected
    if not filePath:
        return

    # Add the vdb extension if needed
    if not filePath.endswith(".vdb"):
        filePath += ".vdb"

    # Creates a maxon.BaseArray with all our obj, we want to convert
    volumesArray = maxon.BaseArray(maxon.frameworks.volume.VolumeRef)
    volumesArray.Resize(len(objList))
    for i, obj in enumerate(objList):
        volumesArray[i] = polygonToVolume(obj)

    # Generates the final file path to save the vdb
    path = maxon.Url(filePath)
    scale = 1.0
    metaData = maxon.DataDictionary()
    try:
        maxon.frameworks.volume.VolumeToolsInterface.SaveVDBFile(path, scale, volumesArray, metaData)
    except IOError:
        raise IOError("Failed to Save the VDB file.")

    print("File saved to ", path)


if __name__ == '__main__':
    main()
