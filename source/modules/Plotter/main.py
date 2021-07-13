import math
from functools import reduce
from matplotlib import pyplot
from source.modules.List.main import List
from source.modules.Measurer.main import Measurer
from source.modules.Plotter.routes import routes
from source.modules.Plotter.distances import distances
from source.modules.Plotter.bearings import bearings
from source.modules.Plotter.deltaBearings import deltaBearings

###
# Interface for plotting dependances such as `route(time)`, `distance(time)`, `bearings(time)`, etc.
##
class Plotter:
    ###
    # Sequence of the line types on the plotted graphs (if there are several graphs on one coords web)
    # @type {List[String]}
    ##
    lineStyles = ['-', '--', '-.']

    ###
    # Plots in (N, E) cartesian coordinate web following:
    # - observing object route
    # - observer object route
    # - calculated observing object route
    # @param {List[List[CartesianRoutePoint]]} paths - observing, observer ans calculated observing object routes
    ##
    @staticmethod
    def routes(paths):
        routes(paths, Plotter.lineStyles)

    ###
    # Plots original and calculated distances in dependance of time
    # @param {List[List[Float]]} dists - original and calculated distances
    ##
    @staticmethod
    def distances(dists):
        distances(dists, Plotter.lineStyles);

    ###
    # Plots bearings in dependance of time
    # @param {List[Integer]} time - timestamps when bearings were measured
    # @param {List[Float]} bearings - bearings to tracking object
    ##
    @staticmethod
    def bearings(time, bearings):
        bearings(time, bearings)
    
    ###
    # Plots differences between prev and current bearing values in dependance on time
    # @param {List[Integer]} time - timestamps when bearings were measured
    # @param {List[Float]} bearings - bearings to tracking object
    ##
    @staticmethod
    def deltaBearings(time, bearings):
        deltaBearings(time, bearings)

    ###
    # Pyplot `figure()` method
    # Allows to plot different graphs on one coordinate web
    ##
    @staticmethod
    def figure():
        pyplot.figure()
    
    ###
    # Pyplot `show()` method
    # Shows all plotted graphs
    ##
    @staticmethod
    def show():
        pyplot.show()
