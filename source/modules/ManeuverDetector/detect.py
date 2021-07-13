import math

###
# Detects object maneuver functional by info about bearings on it and RMS of the noise in bearings measurement
# According to algorithm offerred by G.L. Polyak in "DETERMINING THE COORDINATES AND DRIVING PARAMETERS
# IN MANEUVERING PURPOSE OR PURSUERS" (15)
# @param {Float} bearings - 4 bearings to the object in time
# @param {Float} sigma - RMS of the noise in bearing measurements
# @returns {Boolean} - if object performed maneuver at the moment between 3rd and 4th bearings measured
##
def detect(bearings, sigma):
    A = [
        math.tan(bearings[1] - bearings[0]),
        math.tan(bearings[2] - bearings[0]),
        math.tan(bearings[3] - bearings[0])
    ]
    F = 1 / A[0] - 4 / A[1] + 3/ A[2]
    sigmaF = sigma * math.sqrt((
        (1 / (A[0] ** 2) - 4 / (A[1] ** 2) + 3 / (A[2] ** 2)) ** 2 +
        (1 + 1 / A[0] ** 2) ** 2 +
        16 * (1 + 1 / A[1] ** 2) ** 2 +
        9 * (1 + 1 / A[2] ** 2) ** 2
    ))

    if sigma > 0:
        return abs(F) > 3 * sigmaF
    else:
        return abs(F) > 0.1
