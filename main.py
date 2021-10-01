#Don Lovett
#CS 3642
#main.py
#21 FEB 2021

#Libraries
import cv2 as cv        #openCV used for development
import pyautogui as py  #screenshot and locate functions
import numpy as np      #used for arrays
from python_imagesearch.imagesearch import imagesearcharea  #wrapper for pyautogui
import solve        #used to get a solution to the puzzle
import finish       #used to input the solution into the actual UI

#CONSTANTS
a = 147     #distance in x pixels to the upper left box of the puzzle
b = 327     #distance in y pixels to the upper left box of the puzzle
f = 67      #length and width of the boxes

#9x9 array prefilled with '0's
puzzle = np.zeros((9,9))

#PRECONDITION:
#ubuntu pre-installed sudoku preferrably snapped to
#the left side of the screen
#POSTCONDITION:
#function outputs the pre-defined puzzle array
#full of the numbers from the sudoku puzzle
def gather_nums():

    #iterator
    z = 0

    #loop that finds all the numbers on screen
    #one at a time, then places all the numbers
    #that it found into puzzle[], also prints
    #out what it found when it finds it
    while True:

        #an array full of the reference pictures
        ref = ['nums/one.png', 'nums/two.png', 'nums/three.png',
                'nums/four.png', 'nums/five.png', 'nums/six.png',
                'nums/seven.png', 'nums/eight.png', 'nums/nine.png']

        #an array full of actual numbers
        #that the computer can use
        nums = ['1', '2', '3',
                '4', '5', '6',
                '7', '8', '9']

        #function that locates all of the
        #numbers on screen, coor is a 4-tuple
        #that contains coordinates, length, and hieght
        #the length and height were used in development
        coor = py.locateAllOnScreen(ref[z], confidence=.95)

        #loops through coor to put its
        #values into easier to use variables
        for e in coor:
            x = e[0]    #top left x coordinate of z
            y = e[1]    #top left y coordinate of z

            #fills the array puzzle[]
            puzzle[(y - b)//f][(x - a)//f] = nums[z]

            #prints that it found z at (x, y) to the console
            print("found ", nums[z], " at: ", ((x - a)//f) + 1, ", ", ((y - b)//f) + 1)

        #iterates
        z = z + 1

        #this causes the while statement to
        #finish at z = 8, aka, when it finds
        #all 9 numbers
        if z > 8:
            break

    #prints puzzle[] to the console
    print(puzzle)

#main funtion
def main():

    #initiates gather_nums()
    gather_nums()

    #initiates solve_puzzle()
    if (solve.solve_puzzle(puzzle)):
        
        #prints puzzle[] to the console
        print(puzzle)

        #initiates solve()
        finish.solve(puzzle)

    #prints "all done!" to the console
    print("all done!")

#initiates main()
if __name__ == "__main__":
    main()
