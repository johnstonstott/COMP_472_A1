Assignment 1
Written by Johnston Stott (40059176)
For COMP 472 Section ABIX – Summer 2020

Required Packages
-----------------
- Matplotlib
- Pyshyp
- Numpy

Required Version
----------------
- Python 3

Instructions
------------
1. Install the required packages listed above.
2. In the command line, navigate to the directory containing the main.py file. The
crime_dt data files MUST be in the same directory as main.py, otherwise the program will
not work.
3. Begin the program by running the main.py file with Python. I used the following
command:

python3 main.py

4. Follow the instructions in the command line to complete the execution of the program.
5. To use the program with different inputs, complete execution or exit by pressing
<Ctrl + C> and then run the program again in the same way as in step 3.

Example Program Execution
-------------------------

Below, I have given an example run-through of the program and the format of the accepted
input in case you are getting it incorrect.

-- Montreal Crime Analytics --

Which grid size?
Values less than or equal to 0.002 recommended.
Please type your choice and press enter: 0.002 <Enter>

Which threshold for crime rate?
Enter a percentage between 0 and 100.
Please type your choice and press enter: 80 <Enter>

<The program will open the data file, compute statistics about the data, show the crime
in each block in the command line, and display the map in a new window with the threshold
you provided.>

<When you are done viewing the map, close the window to continue.>

What should the origin be?
Enter in the form '<longitude>, <latitude>'.
Please type your choice and press enter: -73.5872, 45.529 <Enter>

What should the destination be?
Enter in the form '<longitude>, <latitude>'.
Please type your choice and press enter: -73.5508, 45.4932 <Enter>

<The program will show the map again with the shortest path displayed in blue. When you
are done viewing it, you may close the window and the program will terminate.>
