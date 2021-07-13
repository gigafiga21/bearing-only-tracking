###
# Calculates difference between given bearings
# @param {Float} b1 - first bearing
# @param {Float} b2 - second bearing
# @returns {Float}
##
def deltaBearing(b1, b2):
    return (abs(b1 - b2) - 360) % 360

###
# Calculates difference between nearest bearings (previous and current) in `bearings` list
# @param {List[Float]} bearings - bearings
# @returns {List[Float]} - delta bearings (length will be less than `bearings` one on 1 bearing)
##
def deltaBearings(bearings):
    deltaBearings = []
    for p in range(1, len(bearings)):
        deltaBearings.append(deltaBearing(bearings[p - 1], bearings[p]))
    return deltaBearings
