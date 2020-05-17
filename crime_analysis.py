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
    print("Generating crime grid... ", end="")
    # Array to store how many crimes in each block.
    crimes = np.zeros((int(constants.TOT_LON / grid_size), int(constants.TOT_LAT / grid_size)))

    # Go through all crime coordinates, find its block, increment the crime count.
    for i in range(len(lon_list)):
        current_block = find_block(lon_list[i], lat_list[i], grid_size)
        crimes[current_block[0]][current_block[1]] += 1

    print("Done\n")
    return crimes


# Used to determine which block a coordinate belongs to.
def find_block(lon, lat, grid_size):
    diff_lon = lon - constants.MIN_LON
    diff_lat = constants.MAX_LAT - lat
    return [math.floor(diff_lat / grid_size), math.floor(diff_lon / grid_size)]


# Calculate the total count in the crime array.
def calculate_total(array):
    return int(np.sum(array))


# Calculate the average in the crime array.
def calculate_average(array):
    return np.mean(array)


# Calculate the standard deviation in the crime array.
def calculate_stand_dev(array):
    return np.std(array)


# Calculate the median in the crime array.
def calculate_median(array):
    return np.median(array)


# Prints statistics in the console.
def display_stats(array):
    print("Crime statistics for all data:"
          "\nTotal count:", calculate_total(array),
          "\nAverage:", calculate_average(array),
          "\nStandard deviation:", calculate_stand_dev(array),
          "\nMedian:", calculate_median(array))

