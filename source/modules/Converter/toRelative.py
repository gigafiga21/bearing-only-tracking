###
# Recalculates cartesian coords to another coordinate web start point
# @param {List[CartesianRoutePoint]} path - path with coordinate web start to be changed
# @param {CartesianRoutePoint} startPath - new start point of the coordinate web in coords of the one to be changed
# @returns {List[CartesianRoutePoint]}
##
def toRelative(path, startPoint):
    relPath = []

    for point in path:
        relPoint = point.copy()
        relPoint["x"] = relPoint["x"] - startPoint["x"]
        relPoint["y"] = relPoint["y"] - startPoint["y"]
        relPath.append(relPoint);

    return relPath
