import math
import csv
from functools import reduce

###
# Converts read CSV string into data object
# @param {String} path - path to CSV file with data
# @param {Function} method - will be called for each dictionary formed from line of the table (as a `reduce` param)
# @returns {Array[RoutePoint]} - object route
##
def read(path, method):
    with open(path) as dataFile:
        return list(reduce(method, list(csv.DictReader(dataFile, delimiter = ',')), []))
