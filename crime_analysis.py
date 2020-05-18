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
    print("Counting crimes... ", end="")
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
    print("Crime statistics for all blocks:"
          "\nTotal count:", calculate_total(array),
          "\nAverage:", calculate_average(array),
          "\nStandard deviation:", calculate_stand_dev(array),
          "\nMedian:", calculate_median(array),
          "\nNumber of crimes in each block:\n", array, "\n")


# Generates a 2D array of 0's and 1's according to the threshold.
def generate_grid_data(grid_size, threshold, array):
    print(f"Generating grid with grid size {grid_size}, threshold {threshold}%... ", end="")

    # plot_array will store 1 or 0 for above threshold or below threshold.
    array_structure = array.shape
    plot_array = np.zeros(array_structure[0] * array_structure[1])

    # sorted_array is a 1D array sorted min to max.
    flat_array = array.flatten()
    sorted_array = np.sort(array.flatten())

    # Find the index corresponding to the threshold.
    cutoff_index = math.ceil(len(sorted_array) * (threshold / 100))
    cutoff_value = 0

    if cutoff_index < len(sorted_array):
        # If cutoff_index is same as the array index, it means the user put such a high percentage that all blocks are
        # to be considered crime blocks.

        # Find the value at the cutoff index and use it to compare and see which blocks are crime blocks.
        cutoff_value = sorted_array[cutoff_index]

        for i in range(len(flat_array)):
            if flat_array[i] >= cutoff_value:
                plot_array[i] = 1

    plot_array.resize((array_structure[0], array_structure[1]))
    print("Done\n")

    # Print info about blocked areas to user depending on the resulting situation.
    if np.max(plot_array) == 0:
        print("No blocks were marked as high crime areas.\n")
    elif np.min(plot_array) == 1:
        print("All blocks are marked as high crime areas.\n")
    else:
        print("Any block with", int(cutoff_value), "or more crimes is considered a high crime area.\n")

    return plot_array
