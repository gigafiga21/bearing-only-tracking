from source.types.CartesianRoutePoint.main import newCartesianRoutePoint

###
# Titles in the header of CSV tables, keeping cartesian coordinates
# @type {List[String]}
##
header = ["time", "x", "y", "height", "speed"]

###
# Converts dictionary from CSV (with `header` keys) to `CartesianRoutePoint` dictionary
# @param {List[RoutePoint]} acc - array with cartesian points to extend with new one
# @param {Dictionary} pointData - point description from CSV file
# @returns {List[RoutePoint]}
##
def convert(acc, p):
    prevConvertedPoint = acc[len(acc) - 1] if len(acc) > 0 else newCartesianRoutePoint(0, 0, 0, 0)
    acc.append(newCartesianRoutePoint(
        p["time"],
        float(p["dx"]) + prevConvertedPoint["x"],
        float(p["dy"]) + prevConvertedPoint["y"],
        p["speed"]
    ))

    return acc
