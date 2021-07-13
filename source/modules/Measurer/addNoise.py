import numpy
    
###
# Adds noise to given values
# @param {List[FLoat]} path - data to add noise
# @param {Float} sigma - noise RMS
# @returns {List[Float]}
##
def addNoise(path, sigma):
    withNoise = numpy.random.normal(0, sigma, size=len(path))
    for i in range(len(withNoise)):
        withNoise[i] += path[i]
    return withNoise
