# -------------------------------------------------------
# Assignment 1
# Written by Johnston Stott (40059176)
# For COMP 472 Section ABIX – Summer 2020
# --------------------------------------------------------

import math

import constants

import numpy as np


class Node:
    def __init__(self, x, y, is_block):
        self.x = x
        self.y = y
        self.is_block = is_block

    def __str__(self):
        return f"({self.x}, {self.y}) {self.is_block}"


# Creates a 2D array of nodes to be used for path finding.
def generate_grid(crime_data, grid_size):
    # Determine what the dimensions will be based on the grid size. Subtract 1 to account for inaccessible edges.
    x_size = int(constants.TOT_LON / grid_size) - 1
    y_size = int(constants.TOT_LAT / grid_size) - 1

    # Create and fill the list with nodes. Use crime array passed in to see if this is a crime block or not.
    grid = [[None for i in range(0, x_size)] for j in range(0, y_size)]

    for i in range(0, x_size):
        for j in range(0, y_size):
            grid[i][j] = Node(i + 1, j, crime_data[i][j] == 1)

    print(str(grid[0][5]))
    # for j in range(0, y_size):
    #     for i in range(1, x_size + 1):
    #         # print(int(crime_data[i][j]), " ", end="")
    #         grid[i][j] = Node(i, j, crime_data[i][j] == 1)
    #     print("")

# Takes a list [lon, lat] and returns the corresponding grid coordinates based on the grid size.
def coord_to_grid(coords, grid_size):
    # Find x grid.
    x_pos = math.floor((coords[0] - constants.MIN_LON) / grid_size)
    # Find y grid.
    y_pos = math.floor((constants.MAX_LAT - coords[1]) / grid_size)

    return [x_pos, y_pos]


# Takes a list [x, y] and returns the coordinates of this grid (the coordinates of the lower left corner).
def grid_to_coord(grid_pos, grid_size):
    # Find lon coordinate.
    lon_coord = constants.MIN_LON + (grid_pos[0] * grid_size)
    # Find lat coordinate.
    lat_coord = constants.MAX_LAT - (grid_pos[1] * grid_size + grid_size)

    return [lon_coord, lat_coord]
