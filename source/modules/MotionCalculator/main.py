from source.modules.MotionCalculator.maneuverDistance import getParams
from source.modules.MotionCalculator.maneuverDistance import recalculateParams
from source.modules.MotionCalculator.maneuverDistance import maneuverDistance
from source.modules.MotionCalculator.linearDistance import linearDistance

###
# Calculates distances between target and observer objects
##
class MotionCalculator:
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
    @staticmethod
    def getParams(k, T, b0, b1, bk):
        return getParams(k, T, b0, b1, bk)
    
    ###
    # Recalculates `\alpha_0` and `\beta_0` params (from start of the linear trajectory of the target) to
    #   `\alpha_n` and `\beta_n` params calculated in time of the end of the its trajectory
    # @returns {ManeuverParams} - params calculated in time `t` of the end of target's linear trajectory
    ##
    @staticmethod
    def recalculateParams(alpha, beta, t):
        return recalculateParams(alpha, beta, t)

    ###
    # Calculates distance between target and observer objects in the time target object done maneuver
    # @param {ManeuverParams} params1 - params calculated at the start of target's linear trajectory
    # @param {ManeuverParams} params2 - params calculated in time `t` of the end of target's linear trajectory
    # @param {Float} speed - velocity of the observer object
    # @param {Float} H - heading angle (yaw) of the observer object
    # @param {Float} b - bearing to the target object in time of it's maneuver
    # @returns {Float}
    ##
    @staticmethod
    def maneuverDistance(params1, params2, speed, H, b):
        return maneuverDistance(params1, params2, speed, H, b)
    
    ###
    # Calculates distances to tracking object via least-squares approximation with specified initial distance
    # @param {List[CartesianRoutePoint]} points - observer positions from cartesian coordinates related to the start point (`points[0]` has zero coords)
    # @param {List[Float]} bearings - bearings to the observing object measured in `points[]["time"]` time
    # @param {Float} distance - distance between objects in `points[0]["time"]` time
    # @returns {List[Dictionary]} - calculated approximated distances
    ##
    @staticmethod
    def linearDistance(points, bearings, distance):
        return linearDistance(points, bearings, distance)
