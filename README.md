# Bearing only tracking algorithms investigation
Model and realization of the several algorithms for bearing-only tracking automated process for comparing their accuracy.

### Table of contents
1. [Model](#model)  
    1.1. [Input files](#input-files)  

## Model
Model restores traces of the several objects by points given for each and provides access to the positions of all objects in specified time.

### Input files
Input files must be in CSV format with `,` separator (comma). Columns of the table must contain following information in order listed below:
1. `LAT` - latitude coordinate of the object
2. `LNG` - longitude coordinate of the object
3. `SPEED` - speed of the object on the trace segment between current and next specified position
