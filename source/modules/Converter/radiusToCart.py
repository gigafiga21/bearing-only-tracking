import math
from source.types.CartesianRoutePoint.main import newCartesianRoutePoint

###
# Calculates new cartesian coords as the end-point of the vector, defined by its length, start point and angle
# @param {List[Dictionary]} path - vectors descriptions to convert to end-points
# @returns {List[CartesianRoutePoint]}
##
def radiusToCart(radiuses):
    cartPath = []

    for radius in radiuses:
        cartPath.append(newCartesianRoutePoint(
            radius["time"],
            radius["observer"]["x"] + radius["d"] * math.sin(radius["bearing"]),
            radius["observer"]["y"] + radius["d"] * math.cos(radius["bearing"]),
            radius["observer"]["speed"]
        ))
    
    return cartPath