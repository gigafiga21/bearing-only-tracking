import math
from source.types.Earth.main import Earth
from source.types.RoutePoint.main import newRoutePoint
from source.types.ExtendedRoutePoint.main import extendRoutePoint
from source.types.ExtendedRoutePoint.main import newExtendedRoutePoint

###
# Calculates angle speed of the object
# @param {List[RoutePoint|ExtendedRoutePoint]} route - path of the object with point to calculate speed
# @param {Integer} startIndex - index of the point where angle speed will be calculated
# @param {String} axis - `"lat"` or `"lng"`, axis on which speed will be calculated (must be as key in the `route[]` object)
# @returns {Integer}
##
def getAngleSpeed(route, startIndex, axis):
    if len(route) - 2 < startIndex:
        return 0
    return (route[startIndex + 1][axis] - route[startIndex][axis]) / (route[startIndex + 1]["time"] - route[startIndex]["time"])

###
# Finds last initial point in `route` array measured before `time`
# @param {List[RoutePoint|CartesianRoutePoint|ExtendedRoutePoint]} route - route path to scan
# @param {Integer} startIndex - where to start searching
# @param {Integer} time - time to find last point measured before
# @returns {Integer} - index of the desired route point
##
def getLastInit(route, startIndex, time):
    index = startIndex
    while index < len(route):
        if route[index]["time"] >= time:
            return index - 1
        else:
            index += 1

    return len(route) - 1

###
# Extends trajectory composed from the route points of object speed/yaw maneuvers
# @param {List[RoutePoint]} route - path of the object
# @param {Integer} freq - desired time period between two route points
# @returns {List[RoutePoint]}
##
def trace(route, freq):
    escalatedRoute = [route[0]]
    observingTime = route[len(route) - 1]["time"]
    lastInit = extendRoutePoint(0, route[0], route[1])
    angleSpeed = {
        "lat": getAngleSpeed(route, 0, "lat"),
        "lng": getAngleSpeed(route, 0, "lng"),
    }

    # Loop on desired amount of the points
    for cycle in range(1, int(observingTime) // freq + 1):
        # Finding new last point in the original `route` array by time
        newLast = getLastInit(route, lastInit["index"], cycle * freq)
        if newLast > lastInit["index"]:
            lastInit = extendRoutePoint(newLast, route[newLast], route[newLast + 1])
            angleSpeed["lat"] = getAngleSpeed(route, newLast, "lat")
            angleSpeed["lng"] = getAngleSpeed(route, newLast, "lng")
        
        # Calculating params for new polar route point
        lastPassed = escalatedRoute[len(escalatedRoute) - 1]
        stepTime = cycle * freq - lastPassed["time"]
        lat = lastPassed["lat"] + angleSpeed["lat"] * stepTime
        lng = lastPassed["lng"] + angleSpeed["lng"] * stepTime
        escalatedRoute.append(newExtendedRoutePoint(len(escalatedRoute), cycle * freq, lat, lng, lastInit["speed"], lastPassed))
    
    return escalatedRoute
