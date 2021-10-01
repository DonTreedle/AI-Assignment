#finish.py

import pyautogui as py
import numpy as np
import time

#CONSTANTS
a = 20      #serves as a buffer for boundry error
b = 67      #length and width of the boxes
c = 147     #distance in x pixels to the upper left box of the puzzle
d = 327     #distance in y pixels to the upper left box of the puzzle

#an array full of actual numbers
#that the computer can use
nums = ['1', '2', '3',
        '4', '5', '6',
        '7', '8', '9']

#PRECONDITION:
#takes in a 9x9 array, this array
#is the solution to the sudoku puzzle
#POSTCONDITION:
#takes the array and inputs it into
#the GUI of the sudoku puzzle itself
def solve(puzzle):

    #turns the entries in array
    #from string to int
    new_puzzle = puzzle.astype(np.int)

    #iterates through the array and the sudoku
    #puzzle itself to input the answers
    for i in range(9):
        for j in range(9):

            #the solution to block (i, j)
            num = nums[new_puzzle[i][j] - 1]

            #x coordinate of block (i, j)
            x = c + b * j + a

            #y coordinate of block (i, j)
            y = d + b * i + a

            #clicks the block
            py.click(x, y)

            #pauses the program for a bit
            time.sleep(.1)

            #then inputs the numbers through keyboard press
            py.press(num)
