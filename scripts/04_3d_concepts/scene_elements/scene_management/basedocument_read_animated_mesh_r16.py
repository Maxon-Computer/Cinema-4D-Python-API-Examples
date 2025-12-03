"""
Copyright: MAXON Computer GmbH
Author: Maxime Adam, Ferdinand Hoppe

Description:
    - Creates a simple animated deformer rig of a sphere with a bend deformer.
    - Animates a BaseDocument from the min to the max preview range.
    - Creates a Null object for each frame at the position of point 242 of the deformed sphere mesh.

Class/method highlighted:
    - BaseObject.GetDeformCache()
    - c4d.BaseTime()
    - BaseDocument.SetTime()
    - BaseDocument.ExecutePasses()
"""
import c4d

def CreateSetup(doc):
    """Creates a simple animated deformer rig used as an input for the example.

    This can be ignored for the purpose of the example.
    """
    sphere = c4d.BaseObject(c4d.Osphere)
    if not isinstance(sphere, c4d.BaseObject):
        raise MemoryError("Could not create the sphere object.")
    
    bend = c4d.BaseObject(c4d.Obend)
    if not isinstance(bend, c4d.BaseObject):
        raise MemoryError("Could not create the bend deformer.")
    
    bend.InsertUnder(sphere)

    track = c4d.CTrack(
        bend, c4d.DescID(c4d.DescLevel(c4d.BENDOBJECT_STRENGTH, c4d.DTYPE_REAL, 0)))
    if not isinstance(track, c4d.CTrack):
        raise MemoryError("Could not create the CTrack for the bend deformer.")
    
    bend.InsertTrackSorted(track)
    curve = track.GetCurve()
    firstKey = curve.AddKey(doc.GetLoopMinTime())
    if not firstKey:
        raise MemoryError("Could not create the first key for the bend deformer.")
    
    firstKey["key"].SetValue(curve, 0.0)

    secondKey = curve.AddKey(doc.GetLoopMaxTime())
    if not secondKey:
        raise MemoryError("Could not create the second key for the bend deformer.")
    
    secondKey["key"].SetValue(curve, 6.283185307179586)  # 2Pi, i.e., 360°

    doc.InsertObject(sphere)
    doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, sphere)
    return sphere


def main():
    """Main function executing the example.
    """
    # Saves current time
    ctime = doc.GetTime()

    # Retrieve the preview frame range of the document.
    start = doc.GetLoopMinTime().GetFrame(doc.GetFps())
    end = doc.GetLoopMaxTime().GetFrame(doc.GetFps())
    frameRange = end - start + 1

    # Start a stack of undo operations that will be represented as a single undo step.
    doc.StartUndo()

    # Creates a simple setup with an animated deformer.
    sphere = CreateSetup(doc)

    # Loops through the preview frame range.
    for frame in range(start, end + 1):
        # Set the document time to the current frame.
        doc.SetTime(c4d.BaseTime(frame, doc.GetFps()))

        # Build the document to calculate animation, dynamics, expressions, etc., i.e., update the
        # scene to the current time (and with that also build the current deform caches).
        buildflag = c4d.BUILDFLAGS_NONE if c4d.GetC4DVersion() > 20000 else c4d.BUILDFLAGS_0
        doc.ExecutePasses(None, True, True, True, buildflag)

        # Get the deform cache of the sphere. Deform caches only exist on point objects who themselves
        # have a deformer in their hierarchy or who have been built by a generator object which has a
        # deformer in its hierarchy. So, for a sphere, we have to get its cache, which then contains the
        # deformed cache. See the /3d_concepts/modelling/geometry examples for a better understanding 
        # of caches. In modern (2025+) Cinema 4D, we could also just use mxutils.RecurseGraph to simplify
        # cache traversal.
        cache = sphere.GetCache()
        if not isinstance(cache, c4d.PointObject):
            raise RuntimeError("A sphere object should have a point object as its generator cache root.")
        deformCache = cache.GetDeformCache()
        if not isinstance(deformCache, c4d.PointObject):
            raise RuntimeError("This cannot happen, a deform cache is the deformed copy of its host "
                               "object and must alway be a point object.")

        # Calculate the world space position of the point 242 in the deform cache. All points in a
        # point object are always in local space, so we have to multiply it by the global matrix of 
        # the deform cache to get its world space position.
        pos = deformCache.GetPoint(242) * deformCache.GetMg()

        # A gradient value we use to color the nulls based on the frame.
        t = (frame - start) / frameRange

        # Create a null object marker to represent the position of the point at this frame.
        null = c4d.BaseObject(c4d.Onull)
        null[c4d.ID_BASEOBJECT_USECOLOR] = c4d.ID_BASEOBJECT_USECOLOR_ALWAYS
        null[c4d.ID_BASEOBJECT_COLOR] = c4d.Vector(1.0, t, t)
        null[c4d.ID_BASELIST_NAME] = f"Frame {frame} - Point 242"

        # Add an undo item for inserting the null.
        doc.InsertObject(null)
        doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, null)
        null.SetMg(c4d.Matrix(pos))

    # Set the time back to the original time.
    doc.SetTime(ctime)

    # Execute passes once again, to settle simulations and other systems that might need to pass
    # executions. This only has to be done for the last frame when executing passes. And is also
    # not really needed here, as we do not do anything with the scene and it does not contain any
    # complex systems like dynamics.
    buildflag = c4d.BUILDFLAGS_NONE if c4d.GetC4DVersion() > 20000 else c4d.BUILDFLAGS_0
    doc.ExecutePasses(None, True, True, True, buildflag)

    # Finalize all our undo operations as a single step.
    doc.EndUndo()

    # Push an update event to Cinema 4D, so that the UI gets updated.
    c4d.EventAdd(c4d.EVENT_ANIMATE)


if __name__ == "__main__":
    main()
