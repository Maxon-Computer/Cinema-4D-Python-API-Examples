"""Demonstrates handling edges in polygon objects at the example of splitting edges.

The script requires a polygon object with at least one edge selected. The selected edges will be 
split in the middle, into a triangle and a quadrangle, or, when the user is pressing the shift key, 
into three triangles.

Topics:

    * Edge selections and edge indices and their relation to polygons.
    * Geometry operation that require both removing and adding elements.
    * Updating geometry metadata such as selection, vertex maps, vertex colors, and UVW data, here
      at the example of maintaining the data of the split polygons.

Overview:

    When operating on edge selections, one must understand that edges are indexed over polygons. So,
    the edge AB of polygon P is not the same as the edge BA of polygon Q, even though both use the
    same points A and B. This effectively results in the raw edge index formula:

        rawEdgeIndex = polygonIndex * 4 + localEdgeIndex

    which must be often used when working with edges, to convert them into associated polygons or
    points. There exist convenience methods to convert between the raw edge indices and a more
    user-friendly notion of edge indices, such as `PolygonObject.GetSelectedEdges()`, but often
    we must use the raw indices directly, as the user-facing edge indices do not offer that conversion
    relationship.
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2025 MAXON Computer GmbH"
__date__ = "30/05/2025"
__license__ = "Apache-2.0 License"
__version__ = "2024.0.0+"

import c4d

doc: c4d.documents.BaseDocument  # The currently active document.
op: c4d.PolygonObject | None  # The primary selected object in `doc`. Can be `None`.

def main() -> None:
    """Called by Cinema 4D when the script is being executed.
    """
    # Make sure we have a polygon object selected with at least one edge selected. Then figure out
    # if the user is pressing the Shift key to toggle between quadrangle and triangle mode.
    if not isinstance(op, c4d.PolygonObject) or op.GetEdgeS().GetCount() < 1:
        return c4d.gui.MessageDialog("Please select a polygon object with at least one edge selected.")
    
    isQuadMode: bool = True
    state: c4d.BaseContainer = c4d.BaseContainer()
    if (c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.KEY_SHIFT, state)):
        isQuadMode = state[c4d.BFM_INPUT_QUALIFIER] & c4d.QSHIFT != c4d.QSHIFT

    # Edges, as already hinted at in prior geometry examples, do only exist implicitly in the API.
    # Other than for points and polygons, there is no dedicated edge entity in the API. Instead, 
    # edges are defined implicitly by polygons. This also means that edges are indexed over the
    # polygons they belong to. I.e., the edge AB of polygon P is not the same as the edge BA of
    # polygon Q, even tough both use the same points A and B. So, when the user selects a singular 
    # edge in the UI, what is marked in the API as selected, could be one edge (only one polygon uses 
    # these two points forming the edge), two edges (two polygons use these two points to define an 
    # edge) or even more edges (in a non-manifold mesh where many polygons use these two points to 
    # form an edge).

    # There exist convenience methods to translate between the internal raw and the compressed 
    # user-facing edge indices, such as `PolygonObject.GetSelectedEdges()`. But in this case we will
    # use the raw edge indices, as we will have to handle all polygons associated with an edge anyway. 

    # Get the raw edge selection of the object and convert them into a list of raw selected edge 
    # indices. The total number of edges in a mesh is always four times the number of polygons, 
    # because Cinema 4D always stores meshes as sets of quads, even when some of the polygons are 
    # triangles or n-gons.
    activeEdgeSelection: c4d.BaseSelect = op.GetEdgeS()
    edgeCount: int = op.GetPolygonCount() * 4
    selectedEdges: list[int] = [
        i for i, value in enumerate(activeEdgeSelection.GetAll(edgeCount)) if value]

    # Get all the polygons, points, and UVW data of the polygon object.
    polygons: list[c4d.CPolygon] = op.GetAllPolygons()
    points: list[c4d.Vector] = op.GetAllPoints()
    uvwTag: c4d.UVWTag | None = op.GetTag(c4d.Tuvw)
    uvwData: list[list[c4d.Vector]] = [
        list(uvwTag.GetSlow(i).values()) for i in range(uvwTag.GetDataCount())] if uvwTag else []

    # To update geometry by both adding and removing elements, it is often easiest to first 
    # collect and remove all elements that must be removed, to only then add the new elements. 
    # This way we know the final index of everything when we add new data, which is of required. 
    # We therefore establish here #splitData, a container for all the data we have to split, i.e., 
    # remove and then replace with new data. The alternative would be trying to do this in place or
    # creating a 'new' list and then deleting and joining elements at the end. But both would come
    # with the issue that we do not know the final indices of things we add, as we have not yet
    # determined everything that has to be removed.

    # We will use this data structure to store things we have to split, i.e., remove and then later
    # replace by new things. While filling it, we will remove these things from #polygons and 
    # #uvwData.
    splitData: dict[int,                    # Index of the polygon to split.
                    tuple[                  # Data for this split operation.
                        int,                # Local edge in the polygon to split.
                        c4d.CPolygon,       # Polygon to split.
                        list[c4d.Vector]]   # UVW coordinates of the polygon.
                    ] = {}
    
    # --- Remove data to split ---
    
    # Iterate over our raw selected edge indices and and determine the polygon index and local edge
    # their associated with, to then update our data structures.
    for rawEdgeIndex in selectedEdges:
        pid: int = rawEdgeIndex // 4 # The polygon index for the raw edge index. It is the
                                     # integer division of the raw edge index by 4 because each
                                     # polygon has exactly 4 edges. 
                                     # E.g., rawIndex = 9 -> pid = 9 // 2 = 2
        eid: int = rawEdgeIndex % 4  # The index between 0 and 3 inside the polygon referenced by
                                     # the raw edge index. It is the modulo of the raw edge index 
                                     # and 4 because each polygon has exactly 4 edges, so the local 
                                     # edge index is the remainder of the index divided by 4.
                                     # E.g., rawIndex = 9 -> eid = 9 % 2 = 1, where 0 would then mean
                                     # AB, 1 would mean BC, 2 would mean CD and 3 would mean DA.

        # Make sure that we do not try to split the same polygon multiple times.
        if pid in splitData:
            return c4d.gui.MessageDialog(
                f"This edge selection attempts to split the polygon with the ID {pid} more than "
                "once. Doing that is not supported by this script. Please select only select one "
                "edge per polygon.")
        
        # Remove the polygon and uvw data from our things to keep and add them to the list of
        # our to be processed things.
        _pid: int = pid - len(splitData) # Shift the pid by the count of polygons we already removed
        poly: c4d.CPolygon = polygons.pop(_pid)
        uvw: dict[str, c4d.Vector] = uvwData.pop(_pid) if uvwData else []
        splitData[pid] = (eid, poly, uvw)

    # --- Add new data by processing the removed data ---

    # One thing we want to update is the edge selection. Because when we change the polygons, we
    # also change what #activeEdgeSelection means, as these are just indices based on polygon 
    # indices. So, we are going to build a new edge selection based on the new polygons we create.
    newEdgeSelection: list[int] = []

    # The lookup table for the points we create. We will use this to store the mid points of the
    # edges we split, so that we can later update vertex maps and vertex colors by linearly
    # interpolating the values of the two points that were used to create the mid point.
    pointData: dict[int,           # Index of the mid point.
                    list[int, int] # The indices of the two points that were used to create the mid 
                                   # point. I.e., when we later want to update vertex maps or vertex
                                   # colors, we can just linearly interpolate the values of these two
                                   # points to get the value for the mid point.
                    ] = {}

    # Start iterating over the data of the be split polygons we created before, and build the new
    # polygons and UVW data from it. We will also create a new point for the mid point of the edge
    # we split, and store the point indices of the two points that were used to create that mid
    # point in the #pointData dictionary. This way we can later update vertex maps and vertex colors
    # by linearly interpolating the values of the two points that were used to create the mid point.
    for _, (eid, poly, uvw) in splitData.items():
        
        # Get the point indices of the polygon and then shift them by the local edge index, so that
        # our edge #eid to split is always #a - #b. E.g. [A, B, C, D] shifted by eid = 1 --> 
        # [B, C, D, A] or by eid = 2 --> [C, D, A, B]. If you want to, you can also write this as an 
        # if-block.
        polyPointIndices: list[int] = [poly.a, poly.b, poly.c, poly.d]
        a, b, c, d = polyPointIndices[eid:] + polyPointIndices[:eid]

        # Calculate the mid point for the edge AB to split and add it to the list of points, unless 
        # that point already exists from another polygon we handled. #mid is the index of that
        # point to be used by polygons.
        mpoint: c4d.Vector = c4d.utils.MixVec(points[a], points[b], 0.5)
        mid: int = points.index(mpoint) if mpoint in points else len(points)
        pointData[mid] = [a, b]
        points.append(mpoint)

        # Create the new polygons and UVWs for edge we just split.

        lastPid: int = len(polygons) # The ID of the currently last polygon.

        # The user is not pressing Shift, we create a quad and a tri.
        if isQuadMode:
            # Add the new split polygons. As always, order of points - the winding direction - 
            # matters, as it will determine the direction the polygon is facing. See the more basic 
            # polygon examples for details on winding order and how tris and quads are defined.
            polygons += [c4d.CPolygon(a, mid, d, d), # A tri, the last index is repeated.
                         c4d.CPolygon(mid, b, c, d)] # A quad, all indices are unique.
            # UVWs a more or less mirroring the polygons, so we just have to repeat for them, what
            # we did above. Linearly interpolating the UVW coordinates is probably not the best way
            # to do this, but this is just a simple example, so it will do.
            if uvw:
                uva, uvb, uvc, uvd = uvw[eid:] + uvw[:eid]
                uvMid: c4d.Vector = c4d.utils.MixVec(uva, uvb, 0.5)
                uvwData += [[uva, uvMid, uvd, uvd], # the tri
                            [uvMid, uvb, uvc, uvd]] # the quad
        # The user is pressing Shift, so we create three tris instead of a quad and a tri.
        else:
            polygons += [c4d.CPolygon(a, mid, d, d), # These are all tris.
                         c4d.CPolygon(mid, b, c, c),
                         c4d.CPolygon(mid, c, d, d)]
            if uvw:
                uva, uvb, uvc, uvd = uvw[eid:] + uvw[:eid]
                uvMid: c4d.Vector = c4d.utils.MixVec(uva, uvb, 0.5)
                uvwData += [[uva, uvMid, uvd, uvd],
                            [uvMid, uvb, uvc, uvc],
                            [uvMid, uvc, uvd, uvd]]
                
        # Write our new edge selection data. Since we only have to select edges that are topologically
        # part of the old edge, we always only select two edges, no matter if we created two or three
        # polygons. We write the polygons index times four - (lastPid + n) * 4 - offset by the local
        # edge index. Since we shifted our polygons above, so that our edge in question is always
        # AB, we just add 0.
        newEdgeSelection += [(lastPid + 0) * 4 + 0, # Edge AB of the first polygon.
                             (lastPid + 1) * 4 + 0] # Edge AB of the second polygon.

    # --- Update the polygon object by writing our processed data back to it ---

    # Now we write our data back, wrapped into and undo to consolidate all the change we make.
    doc.StartUndo()

    # Write the new points and polygons back to the polygon object.
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, op)
    op.ResizeObject(len(points), len(polygons))
    op.SetAllPoints(points)
    for i, poly in enumerate(polygons):
        op.SetPolygon(i, poly)

    op.Message(c4d.MSG_UPDATE)

    # Now that we have updated the geometry, we can update the edge selection of the object. We can
    # just keep using the selection we accessed at the beginning.
    activeEdgeSelection.DeselectAll()
    for rawEdgeIndex in newEdgeSelection:
        activeEdgeSelection.Select(rawEdgeIndex)

    # We could sanity check our selection with this code. We are writing here a raw selection. So,
    # when there is are the polygons P and Q with a shared edge E, represented by the raw edges
    # Ea and Eb, and we would have only selected Ea, the object would now be in an illegal selection
    # state. Cinema 4D will usually just display an error when that happens, but when there are
    # somewhere unhandled sanity checks, it could crash. We can use our code below to sanity check
    # the selection, but that also costs performance, as we have to Neighbor index he full object. 
    # So, I will not use it here.

    # nbr: c4d.utils.Neighbor = c4d.utils.Neighbor()
    # nbr.Init(op)
    # op.SetSelectedEdges(nbr, activeEdgeSelection, c4d.EDGESELECTIONTYPE_SELECTION)

    # No we start updating the tags we support.

    # Update vertex maps by using our #pointData dictionary to write the linearly interpolated value
    # between the two points we split.
    mapTags: list[c4d.VariableTag] = [t for t in op.GetTags() if t.CheckType(c4d.Tvertexmap)]
    for tag in mapTags:
        # Use the abstract VariableTag interface to access the weight data.
        weights: list[float] = tag.GetAllHighlevelData()
        for mid, (a, b) in pointData.items():
            weights[mid] = c4d.utils.MixNum(weights[a], weights[b], 0.5)

        # Write the modified weights back to the tag and update it.
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, tag)
        tag.SetAllHighlevelData(weights)
        tag.Message(c4d.MSG_UPDATE)

    # Same thing but for vertex colors. We could also use the abstract VariableTag interface
    # here, but since there is a special interface for vertex color tags in Python, we will use 
    # it instead.
    colorTags: list[c4d.VertexColorTag] = [t for t in op.GetTags() if t.CheckType(c4d.Tvertexcolor)]
    for tag in colorTags:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, tag)
        if not tag.IsPerPointColor():
            tag.SetPerPointMode(True)

        data: object = tag.GetDataAddressW()
        for mid, (a, b) in pointData.items():
            aColor: c4d.Vector = tag.GetColor(data, None, None, a)
            aAlpha: float = tag.GetAlpha(data, None, None, a)
            bColor: c4d.Vector = tag.GetColor(data, None, None, b)
            bAlpha: float = tag.GetAlpha(data, None, None, b)
            tag.SetColor(data, None, None, mid, c4d.utils.MixVec(aColor, bColor, 0.5))
            tag.SetAlpha(data, None, None, mid, c4d.utils.MixNum(aAlpha, bAlpha, 0.5))
        
        tag.Message(c4d.MSG_UPDATE)

    # And finally, we update the UVW data, here we just write what we have computed before.
    if uvwTag:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, uvwTag)
        for i, uvw in enumerate(uvwData):
            uvwTag.SetSlow(i, *uvw)

        # Update the tag and the object.
        uvwTag.Message(c4d.MSG_UPDATE)
        op.Message(c4d.MSG_UPDATE)

    # End the undo step and signal Cinema 4D that the viewport and GUI must be updated.
    doc.EndUndo()
    c4d.EventAdd()

if __name__ == '__main__':
    main()