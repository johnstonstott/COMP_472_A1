# -------------------------------------------------------
# Assignment 1
# Written by Johnston Stott (40059176)
# For COMP 472 Section ABIX – Summer 2020
# --------------------------------------------------------

grid_size = 0.0
threshold = 0


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
        reset_values()
        get_user_options()


# Resets values to default in case user needs to restart.
def reset_values():
    global grid_size
    grid_size = 0.0

    global threshold
    threshold = 0
