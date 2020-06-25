# -------------------------------------------------------
# Assignment 1
# Written by Johnston Stott (40059176)
# For COMP 472 Section ABIX – Summer 2020
# --------------------------------------------------------

import os
import sys

import path_finding, crime_analysis, constants, user_options

import shapefile
from matplotlib import pyplot as plt

print("-- Montreal Crime Analytics --")

# Run function in user_options.py to collect values from user.
user_options.get_user_options()

# Open the crime_dt.shp file to read the data.
print("\nOpening data file... ", end="")

if os.path.exists("../data/crime_dt.shp"):
    shp_file = shapefile.Reader("../data/crime_dt.shp", encoding="ISO-8859-1")
    data = shp_file.shapeRecords()
    print("Done\n")
else:
    print("File not found.\nPlease make sure the data files are in the correct folder.")
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

# accessible_grid represents the nodes that can be accessed because they are not edges.
accessible_grid = path_finding.generate_grid(user_options.grid_size)

# Nodes of the origin and destination indicated by the user.
orig_node_pos = path_finding.coord_to_grid([user_options.orig_lon, user_options.orig_lat], user_options.grid_size)
orig_node = path_finding.Node(orig_node_pos[0], orig_node_pos[1])
dest_node_pos = path_finding.coord_to_grid([user_options.dest_lon, user_options.dest_lat], user_options.grid_size)
dest_node = path_finding.Node(dest_node_pos[0], dest_node_pos[1])

# Run A* algorithm located in path_finding.py.
solution_path = path_finding.find_path(orig_node, dest_node, accessible_grid, grid_data)


# Used to show the map with the path.
def show_path(array, path):
    # Store coordinates of solution to display.
    solution_lons = []
    solution_lats = []

    for n in path:
        coords = path_finding.grid_to_coord([n.x_pos, n.y_pos], user_options.grid_size)
        solution_lons.append(coords[0])
        solution_lats.append(coords[1])

    # Display map and overlay path on top.
    if len(path) > 0:
        print("Please close the map when you are done viewing the optimal path.")

        print("\nDisplaying optimal path... ", end="")
        plt.imshow(array, extent=[constants.MIN_LON, constants.MAX_LON, constants.MIN_LAT, constants.MAX_LAT])
        plt.plot(solution_lons, solution_lats)
        plt.show()
        print("Done\n")


# Display map and path overlaid.
show_path(grid_data, solution_path)

print("Program terminating.")
sys.exit(0)
