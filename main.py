# -------------------------------------------------------
# Assignment 1
# Written by Johnston Stott (40059176)
# For COMP 472 Section ABIX – Summer 2020
# --------------------------------------------------------

import os
import sys

import constants
import crime_analysis
import user_options

import shapefile
import numpy as np
from matplotlib import pyplot as plt

print("-- Montreal Crime Analytics --")

# Run function in user_options.py to collect values from user.
# user_options.get_user_options()
user_options.grid_size = 0.002
user_options.metric = "M"
user_options.threshold = 50

# Open the crime_dt.shp file to read the data.
print("\nOpening data file... ", end="")

if os.path.exists("crime_dt.shp"):
    shp_file = shapefile.Reader("crime_dt.shp", encoding="ISO-8859-1")
    data = shp_file.shapeRecords()
    print("Done\n")
else:
    print("File not found.\nPlease make sure the data files are in the same directory as main.py.")
    print("Program terminating.")
    sys.exit(0)

# Read data from file and store coordinates of crimes.
lon_list = []
lat_list = []

for i in range(len(data)):
    lon_list.append(data[i].shape.__geo_interface__["coordinates"][0])
    lat_list.append(data[i].shape.__geo_interface__["coordinates"][1])

# Generate a 2D array and print statistics about the crime data.
crimes = crime_analysis.count_crimes(lon_list, lat_list, user_options.grid_size)
crime_analysis.display_stats(crimes)



plt.imshow(crimes, extent=[constants.MIN_LON, constants.MAX_LON, constants.MIN_LAT, constants.MAX_LAT])

# x1, y1 = [-73.59, -73.55], [45.49, 45.53]
# plt.plot(x1, y1)

plt.show()

print("Done")
