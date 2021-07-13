import math
from source.types.Earth.main import Earth
from source.types.CartesianRoutePoint.main import newCartesianRoutePoint

###
# Converts polar coordinates to cartesian
# @param {List[RoutePoint|ExtendedRoutePoint]} path - path in polar coordinates
# @returns {List[CartesianRoutePoint]}
##
def polToCart(path):
    cartesianPath = []

    for i in range(len(path)):
        point = path[i]
        cartesianPath.append(newCartesianRoutePoint(
            point["time"],
            point["lng"] * Earth["Rla"] * math.cos(point["lat"]),
            point["lat"] * Earth["Rfi"],
            point["speed"]
        ))

    return cartesianPath