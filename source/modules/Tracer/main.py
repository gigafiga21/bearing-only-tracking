from source.modules.Tracer.trace import trace

###
# Interface for increasing density of the route points in object trace
# Adds additional points by using dead reckoning method
##
class Tracer:
    ###
    # Extends trajectory composed from the route points of object speed/yaw maneuvers
    # @param {List[RoutePoint]} route - path of the object
    # @param {Integer} freq - desired time period between two route points
    # @returns {List[RoutePoint]}
    ##
    @staticmethod
    def trace(route, freq):
        if route:
            return trace(route, freq)
