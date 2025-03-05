#coding: utf-8
"""Explains how to generate UVW data for polygon objects.

Can be run as Script Manager script with no scene state requirements.

Topics:
    * Manually creating uvw data via `UVWTag`.
    * Using `CallUVCommand` to use higher level UVW functions built into Cinema 4D.

Examples:
    * GenerateUvwData(): Demonstrates how to generate UVW data for polygon objects.

Overview:
    UV(W) data is a set of coordinates that are used to map a texture onto a polygon object. The
    coordinates are stored in a `UVWTag` instance, which is attached to a `PolygonObject`. Each
    polygon in the object has an uv coordinate for each of its vertices, i.e., the number of uv
    coordinates is four times the polygon count for an object consisting entirely of quads. This 
    also means a vertex can have multiple uv coordinates, one for each polygon it is part of.

See also:
    04_3d_concepts/modeling/uvw_tag : More technical examples for UVW tag. 
    05_modules/bodypaint: More examples for how to deal with UVs and UV commands.
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2025 MAXON Computer GmbH"
__date__ = "05/03/2025"
__license__ = "Apache-2.0 License"
__version__ = "2025.1.0"

import c4d
import typing
import mxutils

doc: c4d.documents.BaseDocument  # The currently active document.
op: typing.Optional[c4d.BaseObject]  # The selected object within that active document. Can be None.

def GenerateUvwData(geometries: tuple[c4d.PolygonObject]) -> None:
    """Demonstrates how to generate UVW data for polygon objects.
    """
    def MapVector(value: c4d.Vector, inMin: c4d.Vector, inMax: c4d.Vector) -> c4d.Vector:
        """Maps a vector from a given range to the values 0 to 1.
        """
        # Put the z component of our input into the x component of the output, because UV are the
        # relevant components for a 2D UV(W) vector, and because the points in the planes in this
        # example lie in the x/z plane, so we move z to y(v) and then leave z(w) empty as we are
        # not generating 3D texture mapping data.
        return c4d.Vector(
            c4d.utils.RangeMap(value.x, inMin.x, inMax.x, 0, 1, True),
            c4d.utils.RangeMap(value.z, inMin.z, inMax.z, 0, 1, True), 0)
    
    def ProjectIntoPlane(p: c4d.Vector, q: c4d.Vector, normal: c4d.Vector) -> c4d.Vector:
        """Projects the point #p orthogonally into the plane defined by #q and #normal.
        """
        # The distance from the point #p to its orthogonal projection #p' on the plane. Or, in short,
        # the length of the shortest path (in Euclidean space) from #p to the plane.
        distance: float = (p - q) * normal
        # Calculate #p' by moving #p #distance units along the inverse plane normal.
        return p - normal * distance

    # Check our inputs for being what we think they are, at least three PolygonObjects.
    mxutils.CheckIterable(geometries, c4d.PolygonObject, minCount=3)

    # Give the three inputs meaningful names.
    plane: c4d.PolygonObject = geometries[0]
    sphere: c4d.PolygonObject = geometries[1]
    cylinder: c4d.PolygonObject = geometries[2]

    # A simple way to generate UVW data is a planar layout which can be directly derived from point 
    # or construction data. An example is of course a plane object, but similar techniques can also 
    # be applied when extruding or lathing/rotating a line, as we then can also associate each point 
    # with a percentage of the total length of the line (u), and a percentage of the total extrusion 
    # height or lathing rotation (v), the uv coordinates of that point.

    # Create a UVW tag for the plane object and get all the points of the plane object.
    uvwTag: c4d.UVWTag = plane.MakeVariableTag(c4d.Tuvw, plane.GetPolygonCount())
    points: typing.List[c4d.Vector] = plane.GetAllPoints()

    # Get the radius of the plane object and iterate over all polygons to calculate the uvw data.
    radius: c4d.Vector = plane.GetRad()
    poly: c4d.CPolygon
    for i, poly in enumerate(plane.GetAllPolygons()):
        # Calculate the uvw data for each point of the polygon. We operate here on the implicit
        # knowledge that the plane object is centered on its origin, e.g., goes form -radius to
        # radius in all three dimensions. We then just map [-radius, radius] to [0, 1], as UV data
        # always 'goes' from 0 to 1. The reason why we always calculate uvw data for four points, 
        # is because Cinema 4D always handles polygons as quads, even if they are triangles or n-gons.
        a: c4d.Vector = MapVector(points[poly.a], -radius, radius)
        b: c4d.Vector = MapVector(points[poly.b], -radius, radius)
        c: c4d.Vector = MapVector(points[poly.c], -radius, radius)
        d: c4d.Vector = MapVector(points[poly.d], -radius, radius)

        # Set the four uvw coordinates for the uvw-polygon #i which corresponds to the geometry 
        # polygon #i.
        uvwTag.SetSlow(i, a, b, c, d)

    # Now we basically do the same for the sphere object. We could also just take the x and z 
    # components of each point to get a top-down uvw projection on the sphere. But we make it a 
    # bit more interesting by projecting each point into a plane defined by the normal of (1, 1, 0), 
    # resulting in planar projection from that angle. This is a bit more formal than projecting by 
    # just discarding a component (the y component in the former case).

    # Our projection orientation and point, there is nothing special about these values, they
    # just look good for this example.
    projectionNormal: c4d.Vector = c4d.Vector(1, 1, 0).GetNormalized()
    projectionOrigin: c4d.Vector = c4d.Vector(0)

    uvwTag: c4d.UVWTag = sphere.MakeVariableTag(c4d.Tuvw, sphere.GetPolygonCount())
    points: typing.List[c4d.Vector] = sphere.GetAllPoints()

    radius: c4d.Vector = sphere.GetRad()
    poly: c4d.CPolygon
    for i, poly in enumerate(sphere.GetAllPolygons()):
        # We project each point of the polygon into the projection plane.
        a: c4d.Vector = ProjectIntoPlane(points[poly.a], projectionOrigin, projectionNormal)
        b: c4d.Vector = ProjectIntoPlane(points[poly.b], projectionOrigin, projectionNormal)
        c: c4d.Vector = ProjectIntoPlane(points[poly.c], projectionOrigin, projectionNormal)
        d: c4d.Vector = ProjectIntoPlane(points[poly.d], projectionOrigin, projectionNormal)

        # We must still map the projected points to the unit square. What we do here is not quite
        # mathematically correct, as there is no guarantee that the projected points have the same
        # bounding box size as the original sphere, but eh, close enough for this example, we at
        # least map all values to [0, 1].
        uvwTag.SetSlow(i, 
                       MapVector(a, -radius, radius), 
                       MapVector(b, -radius, radius),
                       MapVector(c, -radius, radius), 
                       MapVector(d, -radius, radius))
        
    # Lastly, we can use UVCommands to generate UVW data, here at the example of the cylinder object.
    # Doing this comes with the huge disadvantage that we must be in a certain GUI state, i.e., the
    # UV tools only work if the object is in the active document and the UV tools are in a certain
    # state. This makes it impossible to use the UV tools inside a generator object's GetVirtualObjects
    uvwTag: c4d.UVWTag = cylinder.MakeVariableTag(c4d.Tuvw, cylinder.GetPolygonCount())

    # Boiler plate code for UV commands to work, see dedicated #CallUVCommand example for details.
    doc: c4d.documents.BaseDocument = mxutils.CheckType(sphere.GetDocument())
    doc.SetActiveObject(cylinder)

    oldMode: int = doc.GetMode()
    if doc.GetMode() not in [c4d.Muvpoints, c4d.Muvpolygons]:
        doc.SetMode(c4d.Muvpolygons)

    cmdTextureView: int = 170103
    if not c4d.IsCommandChecked(cmdTextureView):
        c4d.CallCommand(cmdTextureView)
        c4d.modules.bodypaint.UpdateMeshUV(False)
        didOpenTextureView = True

    handle: c4d.modules.bodypaint.TempUVHandle = mxutils.CheckType(
        c4d.modules.bodypaint.GetActiveUVSet(doc, c4d.GETACTIVEUVSET_ALL))
    
    # Retrieve the internal UVW data for the current texture view and then invoke
    # the #UVCOMMAND_OPTIMALCUBICMAPPING command, mapping our cylinder object.

    uvw: list[dict] = mxutils.CheckType(handle.GetUVW())
    settings: c4d.BaseContainer = c4d.BaseContainer()
    if not c4d.modules.bodypaint.CallUVCommand(
        handle.GetPoints(), handle.GetPointCount(), handle.GetPolys(), handle.GetPolyCount(),
        uvw, handle.GetPolySel(), handle.GetUVPointSel(), cylinder, handle.GetMode(),
        c4d.UVCOMMAND_OPTIMALCUBICMAPPING, settings):
        raise RuntimeError("CallUVCommand failed.")

    # Write the updated uvw data back.
    if not handle.SetUVWFromTextureView(uvw, True, True, True):
        raise RuntimeError("Failed to write Bodypaint uvw data back.")
    
    c4d.modules.bodypaint.FreeActiveUVSet(handle)
    doc.SetMode(oldMode)

    return

# The following code is boilerplate code to create geometry, generate UVW data for it, and apply 
# materials. It is not relevant for the the subject of UVW mapping.

def BuildGeometry(doc: c4d.documents.BaseDocument) -> tuple[c4d.PolygonObject, c4d.PolygonObject]:
    """Constructs the plane, sphere, and cylinder geometry.
    """
    # Instantiate the generators.
    planeGen: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Oplane), c4d.BaseObject)
    sphereGen: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Osphere), c4d.BaseObject)
    cylinderGen: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocylinder), c4d.BaseObject)

    # Insert the generators into a temporary document to build their caches.
    temp: c4d.documents.BaseDocument = c4d.documents.BaseDocument()
    temp.InsertObject(planeGen)
    temp.InsertObject(sphereGen)
    temp.InsertObject(cylinderGen)
    if not temp.ExecutePasses(None, False, False, True, c4d.BUILDFLAGS_0):
        raise RuntimeError("Could not build the cache for plane and sphere objects.")

    # Retrieve the caches of the generators.
    planeCache: c4d.PolygonObject = mxutils.CheckType(planeGen.GetCache(), c4d.PolygonObject)
    sphereCache: c4d.PolygonObject = mxutils.CheckType(sphereGen.GetCache(), c4d.PolygonObject)
    cylinderCache: c4d.PolygonObject = mxutils.CheckType(cylinderGen.GetCache(), c4d.PolygonObject)

    # Clone the caches and remove the existing UVW tags from the clones.
    plane: c4d.PolygonObject = mxutils.CheckType(planeCache.GetClone(), c4d.PolygonObject)
    sphere: c4d.PolygonObject = mxutils.CheckType(sphereCache.GetClone(), c4d.PolygonObject)
    cylinder: c4d.PolygonObject = mxutils.CheckType(cylinderCache.GetClone(), c4d.PolygonObject)
    for node in [plane, sphere, cylinder]:
        uvwTag: c4d.UVWTag = node.GetTag(c4d.Tuvw)
        if uvwTag:
            uvwTag.Remove()

    # Set the global transform of each of them.
    plane.SetMg(c4d.Matrix(off=c4d.Vector(-300, 0, 0)))
    sphere.SetMg(c4d.Matrix(off=c4d.Vector(0, 0, 0)))
    cylinder.SetMg(c4d.Matrix(off=c4d.Vector(300, 0, 0)))

    # Insert the result the passed document and return them.
    doc.InsertObject(plane)
    doc.InsertObject(sphere)
    doc.InsertObject(cylinder)

    return plane, sphere, cylinder

def ApplyMaterials(geometries: tuple[c4d.PolygonObject]) -> None:
    """Applies a checkerboard material to the given #geometries.
    """
    # Get the document from the geometries and at the same time ensure that the geometries are
    # at least three instances of PolygonObject.
    doc: c4d.documents.BaseDocument = mxutils.CheckIterable(
        geometries, c4d.PolygonObject, minCount=3)[0].GetDocument()

    # Enable the standard renderer in the document.
    renderData: c4d.BaseContainer = doc.GetActiveRenderData()
    renderData[c4d.RDATA_RENDERENGINE] = c4d.RDATA_RENDERENGINE_STANDARD

    # Create the checkerboard material and apply it to the geometries.
    material: c4d.BaseMaterial = mxutils.CheckType(c4d.BaseMaterial(c4d.Mmaterial), c4d.BaseMaterial)
    shader: c4d.BaseShader = mxutils.CheckType(c4d.BaseShader(c4d.Xcheckerboard), c4d.BaseShader)
    doc.InsertMaterial(material)

    material.InsertShader(shader)
    material[c4d.MATERIAL_COLOR_SHADER] = shader
    for geom in geometries:
        materialTag: c4d.BaseTag = geom.MakeTag(c4d.Ttexture)
        materialTag[c4d.TEXTURETAG_MATERIAL] = material
        materialTag[c4d.TEXTURETAG_PROJECTION] = c4d.TEXTURETAG_PROJECTION_UVW

def main(doc: c4d.documents.BaseDocument) -> None:
    """Runs the example.
    """
    # Construct the plane, sphere, and cylinder geometry, then generate the UVW data, and apply a 
    # material to the geometries, finally update the document with #EventAdd. Except for the 
    # #GenerateUvwData call, this is all boilerplate code.
    geometries: tuple[c4d.PolygonObject] = BuildGeometry(doc)
    GenerateUvwData(geometries)
    ApplyMaterials(geometries)

    c4d.EventAdd()

if __name__ == '__main__':
    c4d.CallCommand(13957) # Clear the console.
    # doc is a predefined module attribute as defined at the top of the file.
    main(doc)
