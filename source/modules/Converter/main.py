from source.modules.Converter.cartToPol import cartToPol
from source.modules.Converter.polToCart import polToCart
from source.modules.Converter.radToDeg import radToDeg
from source.modules.Converter.toRelative import toRelative
from source.modules.Converter.radiusToCart import radiusToCart

###
# Interface for coordinates conversions
##
class Converter:
    ###
    # Converts cartesian coordinates to polar
    # @param {List[CartesianRoutePoint]} path - path in cartesian coordinates
    # @returns {List[RoutePoint]}
    ##
    @staticmethod
    def cartToPol(path):
        return cartToPol(path)

    ###
    # Converts polar coordinates to cartesian
    # @param {List[RoutePoint|ExtendedRoutePoint]} path - path in polar coordinates
    # @returns {List[CartesianRoutePoint]}
    ##
    @staticmethod
    def polToCart(path):
        return polToCart(path)
    
    ###
    # Converts polar coordinates from radian to degree units
    # @param {List[RoutePoint|ExtendedRoutePoint]} path - path in polar coordinates in radians
    # @returns {List[RoutePoint|ExtendedRoutePoint]}
    ##
    @staticmethod
    def radToDeg(path):
        return radToDeg(path)

    ###
    # Recalculates cartesian coords to another coordinate web start point
    # @param {List[CartesianRoutePoint]} path - path with coordinate web start to be changed
    # @param {CartesianRoutePoint} startPath - new start point of the coordinate web in coords of the one to be changed
    # @returns {List[CartesianRoutePoint]}
    ##
    @staticmethod
    def toRelative(path, startPoint):
        return toRelative(path, startPoint)
    
    ###
    # Calculates new cartesian coords as the end-point of the vector, defined by its length, start point and angle
    # @param {List[Dictionary]} path - vectors descriptions to convert to end-points
    # @returns {List[CartesianRoutePoint]}
    ##
    @staticmethod
    def radiusToCart(radiuses):
        return radiusToCart(radiuses)
