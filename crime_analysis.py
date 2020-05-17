# -------------------------------------------------------
# Assignment 1
# Written by Johnston Stott (40059176)
# For COMP 472 Section ABIX – Summer 2020
# --------------------------------------------------------

import constants

import numpy as np


# Searches crime data to create a 2D numpy array with the number of crimes in each block.
def count_crimes(lon_list, lat_list, grid_size):
    # Array to store how many crimes in each block.
    crimes = np.zeros((int(constants.TOT_LON / grid_size), int(constants.TOT_LAT / grid_size)))

    # These will be used to compare coordinates and see if a crime is within the block we are looking at.
    start_lon = constants.MIN_LON
    start_lat = constants.MIN_LAT

    # Loop through crime data adding count of crime in each block.
    for i in range(0, 20):
        start_lat += i * grid_size
        end_lat = start_lat + grid_size
        for j in range(0, 20):
            start_lon += j * grid_size
            end_lon = start_lon + grid_size

            # Go through list of crime coordinates and see which are within the block we are evaluating.
            for k in range(0, len(lon_list)):
                print(j, " / ", i, " / ", k, " / ")
                if start_lon <= lon_list[k] < end_lon and start_lat <= lat_list[k] < end_lat:
                    crimes[j][i] += 1

    print(crimes)


# Used to determine which block a coordinate belongs to. Returns a list of [x_coord, y_coord].
def find_block(lon, lat, grid_size):
    diff_lon = lon - constants.MIN_LON
    diff_lat = constants.MAX_LAT - lat
    return [diff_lon / grid_size, diff_lat / grid_size]




