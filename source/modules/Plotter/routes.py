from matplotlib import pyplot
from source.modules.List.main import List

###
# Plots in (N, E) cartesian coordinate web following:
# - observing object route
# - observer object route
# - calculated observing object route
# @param {List[List[CartesianRoutePoint]]} paths - observing, observer ans calculated observing object routes
# @param {List[String]} lineStyles - sequence of the line types on the plotted graphs
##
def routes(paths, lineStyles):
    reducedPaths = list(map(lambda path: List.propsToArray(path, ["x", "y"]), paths))

    for p in range(len(reducedPaths)):
        pyplot.plot(reducedPaths[p][0], reducedPaths[p][1], color='0', linestyle=lineStyles[p % len(lineStyles)])

    pyplot.title("Траектории движения объектов")
    pyplot.grid(True)
    pyplot.legend(['отслеживаемого объекта', 'отслеживающего объекта', 'отслеживаемого объекта оцененная'])
    pyplot.gca().set(xlabel='E, м', ylabel='N, м')
