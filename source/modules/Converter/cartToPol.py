import math
from source.types.Earth.main import Earth
from source.types.RoutePoint.main import newRoutePoint

###
# Converts cartesian coordinates to polar
# @param {List[CartesianRoutePoint]} path - path in cartesian coordinates
# @returns {List[RoutePoint]}
##
def cartToPol(path):
    polarPath = []

    for i in range(len(path)):
        point = path[i]
        fi = point["y"] / Earth["Rfi"]
        polarPath.append(newRoutePoint(
            point["time"],
            fi,
            point["x"] / (Earth["Rla"] * math.cos(fi)),
            point["speed"]
        ))
    
    return polarPath