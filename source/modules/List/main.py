from source.modules.List.propsToArray import propsToArray

###
# Interface for extending amount of possible operations with python `List` type
##
class List:
    ###
    # Converts list of dictionaries to list of lists with selected props
    # @param {List[Dictionary]} data - list to pop values to lists
    # @param {List[String]} keys - keys from `List[Dictionary]`
    # @returns {List[List[*]]} - list with lists of values from `List[Dictionary]` in order of they specified in `keys`
    ##
    @staticmethod
    def propsToArray(data, keys):
        return propsToArray(data, keys)
