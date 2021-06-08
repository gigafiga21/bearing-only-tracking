import source.modules.Loader.polar as Polar
import source.modules.Loader.cartesian as Cartesian
from source.modules.Loader.read import read
from source.modules.Loader.write import write

###
# Interface for loading data from file in CSV format
##
class Loader:
    ###
    # Description of the CSV table header for keeping polar coordinates
    # Titles of the columns in the table
    # @type {List[String]}
    ##
    headerPolar = Polar.header
    
    ###
    # Description of the CSV table header for keeping cartesian coordinates
    # Titles of the columns in the table
    # @type {List[String]}
    ##
    headerCartesian = Cartesian.header

    ###
    # Creates new polar coords point from `pointData` object and appends to `acc`
    # @param {List[RoutePoint]} acc - array with polar points to extend with new one
    # @param {Dictionary} pointData - point description from CSV file
    # @returns {List[RoutePoint]}
    ##
    @staticmethod
    def polar(acc, pointData):
        return Polar.convert(acc, pointData)

    ###
    # Creates new cartesian coords point from `pointData` object and appends to `acc`
    # @param {List[RoutePoint]} acc - array with polar points to extend with new one
    # @param {Dictionary} pointData - point description from CSV file
    # @returns {List[RoutePoint]}
    ##
    @staticmethod
    def cartesian(acc, pointData):
        return Cartesian.convert(acc, pointData)

    ##
    # Reads data from CSV file into list of points
    # @param {String} path - path to CSV file
    # @param {Function} method - `Loader.polar` or `Loader.cartesian` depending on what type (polar or cartesian) of points
    #   are to be read from CSV table
    # @returns {List[RoutePoint]|List[CartesianRoutePoint]}
    ##
    @staticmethod
    def read(path, method = polar):
        if path:
            return read(path, method)
    
    ###
    # Writes list of points into CSV file
    # @param {String} path - path to CSV file
    # @param {List[RoutePoint]|List[CartesianRoutePoint]} - points descriptions to be written
    # @param {List[String]} header - `Loader.headerPolar` or `Loader.headerCartesian` depending on what type of points
    #   are to be written from CSV table
    ##
    @staticmethod
    def write(path, data, header = headerPolar):
        if path:
            return write(path, header, data)
