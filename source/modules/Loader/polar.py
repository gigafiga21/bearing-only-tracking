import math
from source.types.RoutePoint.main import newRoutePoint

###
# Titles in the header of CSV tables, keeping polar coordinates
# @type {List[String]}
##
header = ["time", "lat", "lng", "height", "speed"]

###
# Converts dictionary from CSV (with `header` keys) to `RoutePoint` dictionary
# @param {List[RoutePoint]} acc - array with polar points to extend with new one
# @param {Dictionary} pointData - point description from CSV file
# @returns {List[RoutePoint]}
##
def convert(acc, p):
    acc.append(newRoutePoint(p["time"], float(p["lat"]), float(p["lng"]), p["speed"]))
    return acc
