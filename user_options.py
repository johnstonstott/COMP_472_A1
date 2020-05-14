# -------------------------------------------------------
# Assignment 1
# Written by Johnston Stott (40059176)
# For COMP 472 Section ABIX – Summer 2020
# --------------------------------------------------------

grid_size = 0.0
metric = ""
threshold = 0


# Ask user to specify options and store them.
def get_user_options():
    print("\nWhich grid size?\nValues less than or equal to 0.002 recommended.")
    response = input("Please type your choice and press enter: ")
    global grid_size
    grid_size = float(response)

    print("\nWhich metric for calculating crime rate?\nT for total count, A for average, S for standard deviation, "
          "M for median.")
    response = input("Please type your choice and press enter: ")
    global metric
    metric = str(response)

    print("\nWhich threshold for crime rate?\nEnter a percentage between 0 and 100.")
    response = input("Please type your choice and press enter: ")
    global threshold
    threshold = int(response)

    if metric != "T" and metric != "A" and metric != "S" and metric != "M":
        print("Metric is", metric)
        print("\nInvalid value specified.\n"
              "You must enter 'T', 'A', 'S', or 'M' for the metric.\n"
              "Please try again.")
        reset_values()
        get_user_options()


# Resets values to default in case user needs to restart.
def reset_values():
    global grid_size
    grid_size = 0.0

    global metric
    metric = ""

    global threshold
    threshold = 0
