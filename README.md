# Bearing only tracking algorithms investigation
Model and realization of the several algorithms for bearing-only tracking automated process for comparing their accuracy.

### Table of contents
1. [Setup](#setup)
2. [Model](#model)
    2.1. [Input files](#input-files)

## Setup
This project uses [poetry](https://python-poetry.org/docs/) for managing dependencies. Setup project with following command:
```sh
poetry install
```
If `poetry` is not located by shell but written in `$PATH`, try use `poetry.bat` instead (ocurred on cygwin64 terminal).

## Model
Model restores traces of the several objects by points given for each and provides access to the positions of all objects in specified time.

### Input files
Input files must be in CSV format with `,` separator (comma). Columns of the table must contain following information in order listed below:
1. `LAT` - latitude coordinate of the object
2. `LNG` - longitude coordinate of the object
3. `SPEED` - speed of the object on the trace segment between current and next specified position
Inputted file must contain more than one point description.
