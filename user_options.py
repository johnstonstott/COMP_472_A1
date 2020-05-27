# -------------------------------------------------------
# Assignment 1
# Written by Johnston Stott (40059176)
# For COMP 472 Section ABIX – Summer 2020
# --------------------------------------------------------

import sys

import constants
import path_finding

grid_size = 0.0
threshold = 0
orig_lon = 0.0
orig_lat = 0.0
dest_lon = 0.0
dest_lat = 0.0


# Ask user to specify options and store them.
def get_user_options():
    print("\nWhich grid size?\nValues less than or equal to 0.002 recommended.")
    response = input("Please type your choice and press enter: ")
    global grid_size
    grid_size = float(response)

    print("\nWhich threshold for crime rate?\nEnter a percentage between 0 and 100.")
    response = input("Please type your choice and press enter: ")
    global threshold
    threshold = int(response)

    if threshold < 0 or threshold > 100:
        print("\nInvalid value specified.\n"
              "You must enter a value between 0 and 100.\n"
              "Please try again.")
        reset_user_options()
        get_user_options()


# Resets values to default in case user needs to restart.
def reset_user_options():
    global grid_size
    grid_size = 0.0

    global threshold
    threshold = 0


# Collect and store the begin coordinates for path finding.
def get_orig_coordinates():
    print("\nWhat should the origin be?\nEnter in the form '<longitude>, <latitude>'.")
    response = input("Please type your choice and press enter: ")
    coords = response.split(",")

    # Verify that origin coordinates are within the range of our map.
    if not constants.MIN_LON <= float(coords[0]) <= constants.MAX_LON \
            or not constants.MIN_LAT <= float(coords[1]) <= constants.MAX_LAT:
        print("\nInvalid value(s) specified.\n"
              "The longitude must be between -73.59 and -73.55, and the latitude must be between 45.53 and 45.49.\n"
              "Please try again.")
        # reset_orig_coordinates()
        # get_orig_coordinates()
        sys.exit(0)

    global orig_lon
    orig_lon = float(coords[0])
    global orig_lat
    orig_lat = float(coords[1])

    # Verify that selected coordinates are not on the inaccessible edges.
    global grid_size
    lon_limit = constants.TOT_LON / grid_size - 1
    lat_limit = constants.TOT_LAT / grid_size - 1
    orig_node = path_finding.coord_to_grid([orig_lon, orig_lat], grid_size)

    print(orig_node, " -- ", lon_limit, lat_limit)

    if not 0 < orig_node[0] <= lon_limit or not 0 <= orig_node[1] < lat_limit:
        print("\nInvalid value(s) specified.\n"
              "One of the points corresponds to the boundary edge of the map, which is inaccessible.\n"
              "Please try again.")
        reset_orig_coordinates()
        get_orig_coordinates()


# Collect and store the begin coordinates for path finding.
def get_dest_coordinates():
    print("\nWhat should the destination be?\nEnter in the form '<longitude>, <latitude>'.")
    response = input("Please type your choice and press enter: ")
    coords = response.split(",")

    # Verify that destination coordinates are within the range of our map.
    if not constants.MIN_LON <= float(coords[0]) <= constants.MAX_LON \
            and not constants.MIN_LAT <= float(coords[1]) <= constants.MAX_LAT:
        print("\nInvalid value(s) specified.\n"
              "The longitude must be between -73.59 and -73.55, and the latitude must be between 45.53 and 45.49.\n"
              "Please try again.")
        # reset_dest_coordinates()
        # get_dest_coordinates()
        sys.exit(0)

    global dest_lon
    dest_lon = float(coords[0])
    global dest_lat
    dest_lat = float(coords[1])

    # Verify that selected coordinates are not on the inaccessible edges.
    global grid_size
    lon_nodes = constants.TOT_LON / grid_size
    lat_nodes = constants.TOT_LAT / grid_size
    dest_node = path_finding.coord_to_grid([dest_lon, dest_lat], grid_size)

    if not 0 < dest_node[0] <= lon_nodes or not 0 <= dest_node[1] < lat_nodes:
        print("\nInvalid value(s) specified.\n"
              "One of the points corresponds to the boundary edge of the map, which is inaccessible.\n"
              "Please try again.")
        reset_dest_coordinates()
        get_dest_coordinates()


# Reset to default in case user needs to restart.
def reset_orig_coordinates():
    global orig_lon
    orig_lon = 0.0

    global orig_lat
    orig_lat = 0.0


# Reset to default in case user needs to restart.
def reset_dest_coordinates():
    global dest_lon
    dest_lon = 0.0

    global dest_lat
    dest_lat = 0.0
