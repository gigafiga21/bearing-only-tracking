import csv

###
# Fills CSV file at the `path` path with `data`
# @param {String} path - path to CSV file with data
# @param {List[String]} header - titles in the header of the CSV table, must be presented as keys of the `data` array
# @returns {Array[RoutePoint]} - object route
##
def write(path, header, data):
    with open(path, "w", newline = "") as dataFile:
        writer = csv.DictWriter(dataFile, fieldnames = header)
        writer.writeheader()
        for i in range(len(data)):
            writer.writerow(data[i])
