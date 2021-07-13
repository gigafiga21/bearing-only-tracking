###
# Parameters for calculation distance in the maneuver time of the target 
# @typedef {Dictionary} ManeuverParams
# @prop {Float} alpha - `\alpha_0` parameter
# @prop {Float} beta - `\beta_0` parameter
##

###
# Pseudo constructor for `ManeuverParams`
# @prop {Float} alpha - `\alpha_0` parameter value
# @prop {Float} beta - `\beta_0` parameter value
# @returns {ManeuverParams}
##
def newManeuverParams(alpha, beta):
    return {
        "alpha": float(alpha),
        "beta": float(beta),
    }
