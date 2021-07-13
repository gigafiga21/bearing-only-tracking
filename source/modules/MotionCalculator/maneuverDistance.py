import math
from source.types.ManeuverParams.main import newManeuverParams

###
# Calculates `\alpha_0` and `\beta_0` params for future distance in maneuver point calculation
# Should run after maneuver if trajectory of the target is linear or at the start of calculations
# @param {Float} k - 
# @param {Float} T - period between bearing measurements
# @param {Float} a0 - first bearing of the non-split interval, recorded in time for `\alpha_0` and `\beta_0` calculations
# @param {Float} a1 - second bearing of the non-split interval
# @param {Float} a2 - third bearing of the non-split interval
# @returns {ManeuverParams}
##
def getParams(k, T, b0, b1, bk):
    f = [math.tan(b1 - b0), math.tan(bk - b0)]
    t = [T, T * k]

    alpha = 0
    beta = 0
    if f[0] != 0 and f[1] != 0:
        G = (f[0] * t[1] - f[1] * t[0]) / (f[0] * f[1] * (t[1] - t[0]))
        alpha = - t[0] * (G + 1 / f[0]) / (G ** 2 + 1)
        beta = - G * alpha

    return newManeuverParams(alpha, beta)

###
# Recalculates `\alpha_0` and `\beta_0` params (from start of the linear trajectory of the target) to
#   `\alpha_n` and `\beta_n` params calculated in time of the end of the its trajectory
# @returns {ManeuverParams} - params calculated in time `t` of the end of target's linear trajectory
##
def recalculateParams(alpha, beta, t):
    return newManeuverParams(alpha, beta + t)

###
# Calculates logarithmic value of distance difference
# @param {ManeuverDistance} params - params to calculate value in desired point
# @returns {Float}
##
def logDistance(params):
    return params["beta"] / (params["alpha"] ** 2 + params["beta"] ** 2)

###
# Calculates value of bearing difference
# @param {ManeuverDistance} params - params to calculate value in desired point
# @returns {Float}
##
def logBearing(params):
    return - params["alpha"] / (params["alpha"] ** 2 + params["beta"] ** 2)

###
# Calculates distance between target and observer objects in the time target object done maneuver
# @param {ManeuverParams} params1 - params calculated at the start of target's linear trajectory
# @param {ManeuverParams} params2 - params calculated in time `t` of the end of target's linear trajectory
# @param {Float} speed - velocity of the observer object
# @param {Float} H - heading angle (yaw) of the observer object
# @param {Float} b - bearing to the target object in time of it's maneuver
# @returns {Float}
##
def maneuverDistance(params1, params2, speed, H, b):
    logDist1 = logDistance(params1)
    logDist2 = logDistance(params2)
    logBear1 = logBearing(params1)
    logBear2 = logBearing(params2)
    return (2 * speed * ((logDist2 - logDist1) * math.cos(b - H) - (logBear2 - logBear1) * math.sin(b - H)) /
        (logDist1 ** 2 - logDist2 ** 2 + logBear1 ** 2 - logBear2 ** 2))