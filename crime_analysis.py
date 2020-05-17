# -------------------------------------------------------
# Assignment 1
# Written by Johnston Stott (40059176)
# For COMP 472 Section ABIX – Summer 2020
# --------------------------------------------------------

import math

import constants

import numpy as np


# Searches crime data to create a 2D numpy array with the number of crimes in each block.
def count_crimes(lon_list, lat_list, grid_size):
    # Array to store how many crimes in each block.
    crimes = np.zeros((int(constants.TOT_LON / grid_size), int(constants.TOT_LAT / grid_size)))

    # Go through all crime coordinates, find its block, increment the crime count.
    for i in range(len(lon_list)):
        current_block = find_block(lon_list[i], lat_list[i], grid_size)
        crimes[current_block[0]][current_block[1]] += 1

    return crimes


# Used to determine which block a coordinate belongs to. Returns a list of [x_coord, y_coord].
def find_block(lon, lat, grid_size):
    diff_lon = lon - constants.MIN_LON
    diff_lat = constants.MAX_LAT - lat
    print(math.floor(diff_lon / grid_size), math.floor(diff_lat / grid_size))
    return [math.floor(diff_lon / grid_size), math.floor(diff_lat / grid_size)]




