# -------------------------------------------------------
# Assignment 1
# Written by Johnston Stott (40059176)
# For COMP 472 Section ABIX – Summer 2020
# --------------------------------------------------------

import os
import sys

import shapefile  # Provided by pyshp
import numpy as np
from matplotlib import pyplot

print("-- Montreal Crime Analytics --\n")

# Open the crime_dt.shp file to read the data.
print("Opening data file... ", end="")

if os.path.exists("crime_dt.shp"):
    shp_file = shapefile.Reader("crime_dt.shp", encoding="ISO-8859-1")
    records = shp_file.shapeRecords()
    print("Done\n")
else:
    print("File not found. Please make sure the data files are in the same directory as main.py.")
    print("Program terminating.")
    sys.exit(0)

# x's are -73.59 (west) to -73.55 (east)
x_list = []
# y's are 45.53 (north) to 45.49 (south)
y_list = []

for i in range(len(records)):
    x = records[i].shape.__geo_interface__["coordinates"][0]
    x_list.append(x)
    y = records[i].shape.__geo_interface__["coordinates"][1]
    y_list.append(y)

# print(x_list)
# print(y_list)
# pyplot.scatter(x_list, y_list)
# pyplot.show()

zval = [[0, 0, 1, 1, 0], [1, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 1, 0, 1, 0], [1, 0, 0, 0, 0]]

pyplot.imshow(zval, extent=[-5, 5, -5, 5])

x1, y1 = [-1, 12, 12], [1, 4, 16]

pyplot.plot(x1, y1)

pyplot.show()

print("Done")
