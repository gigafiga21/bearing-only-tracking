###
# @typedef {Dictionary} CartesianRoutePoint
# @prop {Float} time
# @prop {Float} x
# @prop {Float} y
# @prop {Float} speed
##

###
# Pseudo constructor for cartesian route point description dictionary
# @param {*} time - time of the measurement (will be converted to Float)
# @param {*} x - object's x cartesian coord (will be converted to Float)
# @param {*} y - object's y cartesian coord (will be converted to Float)
# @param {*} speed - object's speed at the (x, y) coords (will be converted to Float)
# @returns {CartesianRoutePoint}
##
def newCartesianRoutePoint(time, x, y, speed):
    return {
        "time": float(time),
        "x": float(x),
        "y": float(y),
        "height": 0,
        "speed": float(speed),
    }
