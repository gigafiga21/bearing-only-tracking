import math

###
# Converts polar coordinates from radian to degree units
# @param {List[RoutePoint|ExtendedRoutePoint]} path - path in polar coordinates in radians
# @returns {List[RoutePoint|ExtendedRoutePoint]}
##
def radToDeg(path):
    degPath = []

    for i in range(len(path)):
        point = path[i].copy()
        point["lat"] = point["lat"] * 180 / math.pi
        point["lng"] = point["lng"] * 180 / math.pi
        degPath.append(point)

    return cartesianPath