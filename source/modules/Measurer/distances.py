import math

###
# Calculates distance between cartesian points
# @param {CartesianRoutePoint} Acart - first point coords
# @param {CartesianRoutePoint} Bcart - second point coords
# @returns {Float}
##
def distance(Acart, Bcart):
    return {
        "time": Acart["time"],
        "d": math.sqrt((Acart["x"] - Bcart["x"]) ** 2 + (Acart["y"] - Bcart["y"]) ** 2)
    }

###
# Calculates distances between pairs of cartesian points of given tracks sequentially
# @param {List[CartesianRoutePoint]} trackA - first path
# @param {List[CartesianRoutePoint]} trackB - second path
# @returns {List[Float]}
##
def distances(trackA, trackB):
    distances = []
    for p in range(len(trackA)):
        distances.append(distance(trackA[p], trackB[p]))
    return distances