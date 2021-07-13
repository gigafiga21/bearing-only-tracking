import math
from matplotlib import pyplot

###
# Plots bearings in dependance of time
# @param {List[Integer]} time - timestamps when bearings were measured
# @param {List[Float]} bearings - bearings to tracking object
##
def bearings(time, bearings):
    pyplot.plot(time, list(map(lambda b: b * 180 / math.pi, bearings)), color='0')