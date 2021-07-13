import math
from source.modules.Converter.main import Converter

###
# Calculates bearing from `Apol` to `Bpol`
# @param {RoutePoint|ExtendedRoutePoint} Apol - route point of the object measures bearing
# @param {RoutePoint|ExtendedRoutePoint} Bpol - route point of the tracking object
# @returns {Float}
##
def bearing(Apol, Bpol):
    # dFi = Apol["lat"] - Bpol["lat"]
    # dLa = Apol["lng"] - Bpol["lng"]
    # dY = math.sqrt(2 * Earth["Rfi"] ** 2 * (1 - math.cos(dFi)))
    # dX = math.sqrt(2 * Earth["Rla"] ** 2 * (1 - math.cos(dLa)))
    # return (math.pi + math.atan2(dLa * Earth["Rla"], dFi * Earth["Rfi"])) % (2 * math.pi)
    [A, B] = Converter.polToCart([Apol, Bpol])
    return (math.pi + math.atan2(A["x"] - B["x"], A["y"] - B["y"])) % (2 * math.pi)

###
# Calculates bearings from each pair of `trackA` and `trackB` points sequentially
# @param {List[RoutePoint|ExtendedRoutePoint]} Apol - route points of the object measures bearing
# @param {List[RoutePoint|ExtendedRoutePoint]} Bpol - route points of the tracking object
# @returns {List[Float]}
##
def bearings(trackA, trackB):
    bearings = []
    for p in range(len(trackA)):
        bearings.append(bearing(trackA[p], trackB[p]))
    return bearings