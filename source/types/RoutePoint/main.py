###
# @typedef {Dictionary} RoutePoint
# @prop {Float} time
# @prop {Float} lat
# @prop {Float} lng
# @prop {Float} speed
##

###
# Pseudo constructor for polar route point description dictionary
# @param {*} time - time of the measurement (will be converted to Float)
# @param {*} lat - object's latitude (will be converted to Float)
# @param {*} lng - object's longitude (will be converted to Float)
# @param {*} speed - object's speed at the (x, y) coords (will be converted to Float)
# @returns {CartesianRoutePoint}
##
def newRoutePoint(time, lat, lng, speed):
    return {
        "time": float(time),
        "lat": float(lat),
        "lng": float(lng),
        "height": 0,
        "speed": float(speed),
    }
