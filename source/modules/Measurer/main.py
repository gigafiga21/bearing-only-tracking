import math
import numpy
from source.types.Earth.main import Earth
from source.modules.Converter.main import Converter
from source.modules.Measurer.bearings import bearings
from source.modules.Measurer.deltaBearings import deltaBearings
from source.modules.Measurer.addNoise import addNoise
from source.modules.Measurer.distances import distances

###
# Interface for "measuring" functional
##
class Measurer:
    ###
    # Calculates bearings from each pair of `trackA` and `trackB` points sequentially
    # @param {List[RoutePoint|ExtendedRoutePoint]} Apol - route points of the object measures bearing
    # @param {List[RoutePoint|ExtendedRoutePoint]} Bpol - route points of the tracking object
    # @returns {List[Float]}
    ##
    @staticmethod
    def bearings(trackA, trackB):
        return bearings(trackA, trackB);

    ###
    # Calculates difference between nearest bearings (previous and current) in `bearings` list
    # @param {List[Float]} bearings - bearings
    # @returns {List[Float]} - delta bearings (length will be less than `bearings` one on 1 bearing)
    ##
    @staticmethod
    def deltaBearings(bearings):
        return deltaBearings(bearings)

    ###
    # Calculates distances between pairs of cartesian points of given tracks sequentially
    # @param {List[CartesianRoutePoint]} trackA - first path
    # @param {List[CartesianRoutePoint]} trackB - second path
    # @returns {List[Float]}
    ##
    @staticmethod
    def distances(trackA, trackB):
        return distances(trackA, trackB)
    
    ###
    # Adds noise to given values
    # @param {List[FLoat]} path - data to add noise
    # @param {Float} sigma - noise RMS
    # @returns {List[Float]}
    ##
    @staticmethod
    def addNoise(path, sigma):
        return addNoise(path, sigma)

