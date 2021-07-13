import math
from matplotlib import pyplot
from source.modules.Measurer.main import Measurer

###
# Plots differences between prev and current bearing values in dependance on time
# @param {List[Integer]} time - timestamps when bearings were measured
# @param {List[Float]} bearings - bearings to tracking object
##
def deltaBearings(time, bearings):
    pyplot.plot(time[1:], list(map(lambda b: b * 180 / math.pi, Measurer.deltaBearings(bearings))), color='0')
    
    pyplot.title("Изменения пеленга")
    pyplot.grid(True)
    pyplot.gca().set(xlabel='Время, с', ylabel='Изменения пеленга, °')
