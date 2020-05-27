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
import path_finding

import shapefile
import numpy as np
from matplotlib import pyplot as plt

print("-- Montreal Crime Analytics --")

# Run function in user_options.py to collect values from user.
# user_options.get_user_options()
user_options.grid_size = 0.002
user_options.threshold = 80

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

# Generate array to use to display grid, depending on user options.
grid_data = crime_analysis.generate_grid_data(user_options.grid_size, user_options.threshold, crimes)


# Used to show the grid with no path.
def show_grid(array):
    print("Displaying generated grid... ", end="")
    plt.imshow(array, extent=[constants.MIN_LON, constants.MAX_LON, constants.MIN_LAT, constants.MAX_LAT])
    plt.show()
    print("Done")


# Display the grid.
show_grid(grid_data)

# Ask for a starting and ending coordinate for A* path finding.
user_options.get_orig_coordinates()
user_options.get_dest_coordinates()

print(user_options.orig_lon, user_options.orig_lat, user_options.dest_lon, user_options.dest_lat)

# x1, y1 = [-73.59, -73.55], [45.49, 45.53]
# plt.imshow(grid_data, extent=[constants.MIN_LON, constants.MAX_LON, constants.MIN_LAT, constants.MAX_LAT])
# plt.plot(x1, y1)
# plt.show()
