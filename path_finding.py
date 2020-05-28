# -------------------------------------------------------
# Assignment 1
# Written by Johnston Stott (40059176)
# For COMP 472 Section ABIX – Summer 2020
# --------------------------------------------------------

import math
from queue import PriorityQueue

import constants


class Node:
    def __init__(self, x_pos, y_pos, is_block):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.is_block = is_block
        self.f = 0
        self.g = 0
        self.h = 0
        self.prev = []

    def __str__(self):
        return f"({self.x_pos}, {self.y_pos}, {len(self.prev)})"

    # This is so when we add a Node to PriorityQueue, de-queueing returns the node with the lowest f value.
    def __lt__(self, other):
        return self.f < other.f


def find_path(orig, dest, node_grid, crime_grid):
    # To store nodes that we need to visit.
    open_list = PriorityQueue()
    open_list.put(orig)

    # To store nodes that have been visited already.
    closed_list = []

    while len(open_list.queue) > 0:
        # Retrieves the node with the lowest f.
        curr = open_list.get()
        curr.prev.append(curr)

        # Found a path to the solution, so return a list of predecessors to this node.
        if is_goal(curr, dest):
            print("The optimal path has been found")
            return curr.prev

        # Search the surrounding nodes of current.
        neighbours = find_neighbours(curr, node_grid)
        closed_list.append(curr)

        for n in neighbours:
            # Eliminate nodes that are not reachable.
            if calculate_cost(curr, n, crime_grid) == -1:
                neighbours.remove(n)
                continue

            # Compute scores of the nodes.
            n.g = curr.g + calculate_cost(curr, n, crime_grid)
            n.h = calculate_h(n, dest)
            n.f = n.g + n.h

            # Add them to the open list.
            if n not in open_list.queue:
                n.prev = n.prev + curr.prev
                open_list.put(n)


    print("The optimal path is not found.")
    return []


# Calculates the cost to go from one node to the other. Returns -1 if this is an invalid path (passes over a block).
def calculate_cost(node_a, node_b, crime_grid):
    # Check for None nodes.
    if node_a is None or node_b is None:
        return -1

    # Check for non-neighbouring nodes.
    if abs(node_a.x_pos - node_b.x_pos) > 1 or abs(node_a.y_pos - node_b.y_pos) > 1:
        return -1

    # Check for same node.
    if node_a.x_pos == node_b.x_pos and node_a.y_pos == node_b.y_pos:
        return -1

    grid_up_left = crime_grid[node_a.x_pos - 1][node_a.y_pos]
    grid_up_right = crime_grid[node_a.x_pos][node_a.y_pos]
    grid_down_left = crime_grid[node_a.x_pos - 1][node_a.y_pos - 1]
    grid_down_right = crime_grid[node_a.x_pos][node_a.y_pos - 1]

    # Vertical up move.
    if node_a.x_pos == node_b.x_pos and node_a.y_pos == (node_b.y_pos + 1):
        if grid_up_left == 1 and grid_up_right == 1:
            return -1
        elif (grid_up_left == 0 and grid_up_right == 1) or (grid_up_left == 1 and grid_up_right == 1):
            return 1.3
        elif grid_up_left == 0 and grid_up_right == 0:
            return 1

    # Vertical down move.
    if node_a.x_pos == node_b.x_pos and node_a.y_pos == (node_b.y_pos - 1):
        if grid_down_left == 1 and grid_down_right == 1:
            return -1
        elif (grid_down_left == 0 and grid_down_right == 1) or (grid_down_left == 1 and grid_down_right == 0):
            return 1.3
        elif grid_down_left == 0 and grid_down_right == 0:
            return 1

    # Horizontal left move.
    if node_a.y_pos == node_b.y_pos and node_a.x_pos == (node_b.x_pos + 1):
        if grid_up_left == 1 and grid_down_left == 1:
            return -1
        elif (grid_up_left == 0 and grid_down_left == 1) or (grid_up_left == 1 and grid_down_left == 0):
            return 1.3
        elif grid_up_left == 0 and grid_down_left == 0:
            return 1

    # Horizontal right move.
    if node_a.y_pos == node_b.y_pos and node_a.x_pos == (node_b.x_pos - 1):
        if grid_up_right == 1 and grid_down_right == 1:
            return -1
        elif (grid_up_right == 0 and grid_down_right == 1) or (grid_up_right == 1 and grid_down_right == 0):
            return 1.3
        elif grid_up_right == 0 and grid_down_right == 0:
            return 1

    # Diagonal up left move.
    if node_a.x_pos == (node_b.x_pos + 1) and node_a.y_pos == (node_b.y_pos + 1):
        if grid_up_left == 1:
            return -1
        elif grid_up_left == 0:
            return 1.5

    # Diagonal up right move
    if node_a.x_pos == (node_b.x_pos - 1) and node_a.y_pos == (node_b.y_pos + 1):
        if grid_up_right == 1:
            return -1
        elif grid_up_right == 0:
            return 1.5

    # Diagonal down left move.
    if node_a.x_pos == (node_b.x_pos + 1) and node_a.y_pos == (node_b.y_pos - 1):
        if grid_down_left == 1:
            return -1
        elif grid_down_left == 0:
            return 1.5

    # Diagonal down right move.
    if node_a.x_pos == (node_b.x_pos - 1) and node_a.y_pos == (node_b.y_pos - 1):
        if grid_down_right == 1:
            return -1
        elif grid_down_right == 0:
            return 1.5


# Look in all directions and if there is a node there (not out of bounds), then add it and return the list.
def find_neighbours(node, node_grid):
    neighbours = []

    x_index = node.x_pos - 1
    y_index = node.y_pos
    x_size = len(node_grid)
    y_size = len(node_grid[0])

    # Up left.
    if 0 <= x_index - 1 < x_size and 0 <= y_index < y_size:
        neighbour = node_grid[x_index - 1][y_index - 1]
        neighbours.append(neighbour)

    # Up.
    if 0 <= x_index < x_size and 0 <= y_index - 1 < y_size:
        neighbour = node_grid[x_index][y_index - 1]
        neighbours.append(neighbour)

    # Up right.
    if 0 <= x_index + 1 < x_size and 0 <= y_index - 1 < y_size:
        neighbour = node_grid[x_index + 1][y_index - 1]
        neighbours.append(neighbour)

    # Left.
    if 0 <= x_index - 1 < x_size and 0 <= y_index < y_size:
        neighbour = node_grid[x_index - 1][y_index]
        neighbours.append(neighbour)

    # Right.
    if 0 <= x_index + 1 < x_size and 0 <= y_index < y_size:
        neighbour = node_grid[x_index + 1][y_index]
        neighbours.append(neighbour)

    # Down left.
    if 0 <= x_index - 1 < x_size and 0 <= y_index + 1 < y_size:
        neighbour = node_grid[x_index - 1][y_index + 1]
        neighbours.append(neighbour)

    # Down.
    if 0 <= x_index < x_size and 0 <= y_index + 1 < y_size:
        neighbour = node_grid[x_index][y_index + 1]
        neighbours.append(neighbour)

    # Down right.
    if 0 <= x_index + 1 < x_size and 0 <= y_index + 1 < y_size:
        neighbour = node_grid[x_index + 1][y_index + 1]
        neighbours.append(neighbour)

    return neighbours


# Constructs a list of nodes along the path from the node passed as an argument.
def revisit_path(node):
    path = []

    curr = node
    path.append(curr)

    # Once we arrive at a node with prev None, this is the starting node.
    while curr.prev is not None:
        prev = curr.prev
        print(prev)
        path.append(prev)
        curr = prev

    return path


# Creates a 2D array of nodes to be used for path finding.
def generate_grid(crime_data, grid_size):
    # Determine what the dimensions will be based on the grid size. Subtract 1 to account for inaccessible edges.
    x_size = int(constants.TOT_LON / grid_size) - 1
    y_size = int(constants.TOT_LAT / grid_size) - 1

    # Create and fill the list with nodes. Use crime array passed in to see if this is a crime block or not.
    grid = [[None for i in range(0, x_size)] for j in range(0, y_size)]

    for i in range(0, x_size):
        for j in range(1, y_size + 1):
            grid[j - 1][i] = Node(j, i, crime_data[i][j] == 1)

    return grid


# Heuristic function to estimate the cost between the current node and the goal node.
# It does this by comparing the positions of the two nodes and determining how many vertical, horizontal, or diagonal
# moves are needed to get there if there were no blocks in the way.
# By doing it this way, we ensure that the heuristic is never overestimated.
def calculate_h(node, goal):
    hor_diff = abs(node.x_pos - goal.x_pos)
    ver_diff = abs(node.y_pos - goal.y_pos)

    # The current node and goal node are aligned vertically. Can get there with straight line.
    if hor_diff == 0:
        return 1 * ver_diff
    # The current node and goal node are aligned horizontally. Can get there with straight line.
    elif ver_diff == 0:
        return 1 * hor_diff
    # Only need to move horizontally to get there.
    elif hor_diff == ver_diff:
        return 1.5 * hor_diff
    # Need to move more horizontally than vertically.
    elif hor_diff > ver_diff:
        diff = hor_diff - ver_diff
        return diff * 1 + ver_diff * 1.5
    # Need to move more vertically than horizontally.
    elif ver_diff > hor_diff:
        diff = ver_diff - hor_diff
        return diff * 1 + hor_diff * 1.5


# To determine if a certain node is the goal node.
def is_goal(node, goal):
    return node.x_pos == goal.x_pos and node.y_pos == goal.y_pos


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
