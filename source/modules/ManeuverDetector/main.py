from source.modules.ManeuverDetector.detect import detect

###
# Interface with detecting object's maneuver functional
##
class ManeuverDetector:
    ###
    # Detects object maneuver functional by info about bearings on it and RMS of the noise in bearings measurement
    # According to algorithm offerred by G.L. Polyak in "DETERMINING THE COORDINATES AND DRIVING PARAMETERS
    # IN MANEUVERING PURPOSE OR PURSUERS" (15)
    # @param {Float} bearings - 4 bearings to the object in time
    # @param {Float} sigma - RMS of the noise in bearing measurements
    # @returns {Boolean} - if object performed maneuver at the moment between 3rd and 4th bearings measured
    ##
    @staticmethod
    def detect(bearings, sigma):
        return detect(bearings, sigma)
