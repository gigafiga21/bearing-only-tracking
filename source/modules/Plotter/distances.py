from matplotlib import pyplot
from source.modules.List.main import List

###
# Plots original and calculated distances in dependance of time
# @param {List[List[Float]]} distances - original and calculated distances
##
def distances(distances, lineStyles):
    reducedDistances = list(map(lambda distance: List.propsToArray(distance, ["time", "d"]), distances))

    for d in range(len(reducedDistances)):
        pyplot.plot(reducedDistances[d][0], reducedDistances[d][1], color='0', linestyle=lineStyles[d % len(lineStyles)])
    
    pyplot.title("Дистанция")
    pyplot.grid(True)
    pyplot.legend(['истинная', 'вычисленная'])
    pyplot.gca().set(xlabel='Время, с', ylabel='Дистанция, м')