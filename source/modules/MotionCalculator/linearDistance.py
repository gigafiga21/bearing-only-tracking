import math
import numpy

###
# Calculates vector of target object speed estimations: `\Theta^\^ = [(V^t)_E, (V^t)_N]`
# @param {List[CartesianRoutePoint]} points - points of trajectory of the observer object on the period when observing object trajectory is linear
# @param {List[Float]} bearings - bearings to the observer object when its trajectory is linear
# @param {Float} distance - distance between objects on the start of measurements (on `points[0]["time"]`)
# @returns {List[Float]} - estimated E and N velocity projections of the target 
##
def getConsts(points, bearings, distance):
    a = numpy.array([[
        (points[i]["time"] - points[0]["time"]) * math.cos(bearings[i]),
        - (points[i]["time"] - points[0]["time"]) * math.sin(bearings[i])
    ] for i in range(1, len(points))])
    b = [points[i]["x"] * math.cos(bearings[i]) - points[i]["y"] * math.sin(bearings[i]) - math.sin(bearings[0] - bearings[i]) * distance for i in range(1, len(points))]
    k = numpy.matmul(numpy.linalg.inv(numpy.matmul(numpy.transpose(a), a)), numpy.transpose(a))
    return numpy.matmul(k, b)

###
# Calculates distances to tracking object via least-squares approximation with specified initial distance
# @param {List[CartesianRoutePoint]} points - observer positions from cartesian coordinates related to the start point (`points[0]` has zero coords)
# @param {List[Float]} bearings - bearings to the observing object measured in `points[]["time"]` time
# @param {Float} distance - distance between objects in `points[0]["time"]` time
# @returns {List[Dictionary]} - calculated approximated distances
##
def linearDistance(points, bearings, distance):
    consts = getConsts(points, bearings, distance)
    if consts is None:
        return None

    lastPoint = len(points) - 1
    return {
        "yaw": math.atan2(consts[1], consts[0]),
        "speed": math.sqrt(consts[0] ** 2 + consts[1] ** 2),
        "d": (distance * math.sin(bearings[0]) + consts[0] * (points[lastPoint]["time"] - points[0]["time"]) - points[lastPoint]["x"]) / math.sin(bearings[lastPoint])
    }
