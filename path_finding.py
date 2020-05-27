# -------------------------------------------------------
# Assignment 1
# Written by Johnston Stott (40059176)
# For COMP 472 Section ABIX – Summer 2020
# --------------------------------------------------------

import math

import constants


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
