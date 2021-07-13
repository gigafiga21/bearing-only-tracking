###
# Converts list of dictionaries to list of lists with selected props
# @param {List[Dictionary]} data - list to pop values to lists
# @param {List[String]} keys - keys from `List[Dictionary]`
# @returns {List[List[*]]} - list with lists of values from `List[Dictionary]` in order of they specified in `keys`
##
def propsToArray(data, keys):
    convertedValues = list(map(lambda key: [], keys))

    for values in data:
        for keysCounter in range(len(keys)):
            convertedValues[keysCounter].append(values[keys[keysCounter]])
    
    return convertedValues
