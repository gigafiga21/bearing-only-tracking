import math
from source.types.Earth.main import Earth
from source.types.RoutePoint.main import newRoutePoint

###
# @typedef {RoutePoint&Dictionary} ExtendedRoutePoint
# @prop {Integer} index
# @prop {Float} yaw 
##

###
# Extends `RoutePoint` dict to `ExtendedRoutePoint`
# @param {Integer} index - service info
# @param {RoutePoint} A - route point to be extended
# @param {RoutePoint} B - next route point (in time, for calculating yaw)
# @returns {ExtendedRoutePoint}
##
def extendRoutePoint(index, A, B):
    extended = A.copy()
    extended.update({
        "index": index,
        "yaw": (math.pi + math.atan2((B["lng"] - A["lng"]) * Earth["Rla"], (B["lat"] - A["lat"]) * Earth["Rfi"])) % (2 * math.pi)
    })

    return extended

###
# Pseudo constructor for extended version of polar route point description dictionary
# @param {*} index - service info (will be converted to Integer)
# @param {*} time - time of the measurement (will be converted to Float)
# @param {*} lat - object's latitude (will be converted to Float)
# @param {*} lng - object's longitude (will be converted to Float)
# @param {*} speed - object's speed at the (x, y) coords (will be converted to Float)
# @param {*} other - next route point on the object trajectory (for calculating yaw, etc.)
# @returns {ExtendedRoutePoint}
##
def newExtendedRoutePoint(index, time, lat, lng, speed, other):
    point = newRoutePoint(time, lat, lng, speed)
    return extendRoutePoint(index, point, other)
