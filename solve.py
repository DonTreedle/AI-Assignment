#solve.py
#DISCLAIMER:
#I did NOT create this algorithm
#it is called the backtraking algorithm
#and was found here: https://www.geeksforgeeks.org/sudoku-backtracking-7/
#I did however fit the algorithm to what i needed

import numpy as np

#PRECONDITION:
#takes prefilled array puzzle[]
#and finds the empty entries
#POSTCONDITION:
#returns True and the location
#of an empty entry, if not then
#it just returns False
def find_empty(puzzle, empty):
    for i in range(9):
        for j in range(9):
            if (puzzle[i][j] == 0):
                empty[0] = i
                empty[1] = j
                return True
    return False

#PRECONDITION:
#takes an array, the row its checking
#and the number its checking for
#POSTCONDITION:
#if the number was used in the row
#the funtion returns True, if not
#it returns False
def usedIn_row(puzzle, row, num):
    for i in range(9):
        if (puzzle[row][i] == num):
            return True
    return False

#PRECONDITION:
#takes an array, the column its checking
#and the number its checking for
#POSTCONDITION:
#if the number was used in the colomn
#the funtion returns True, if not
#it returns False
def usedIn_col(puzzle, col, num):
    for j in range(9):
        if (puzzle[j][col] == num):
            return True
    return False

#PRECONDITION:
#takes an array, the box its checking
#and the number its checking for
#POSTCONDITION:
#if the number was used in the box
#the funtion returns True, if not
#it returns False
def usedIn_box(puzzle, row, col, num):
    for i in range(3):
        for j in range(3):
            if (puzzle[row + i][col + j] == num):
                return True
    return False

#PRECONDITION:
#takes an array, the row, column,
#and number that its checking for
#POSTCONDITION:
#executes and returns the truth
#value of usedIn_row(), usedIn_col,
#and usedIn_box
#essentials checks the validity of
#the number in question
def safe_space(puzzle, row, col, num):
    return not usedIn_row(puzzle, row, num) and not usedIn_col(puzzle, col, num) and not usedIn_box(puzzle, row - row % 3, col - col % 3, num)

#recursive funtion that creates a colution the problem
#PRECONDTION:
#takes a partially filled 9x9 array
#POSTCONDITION:
#outputs the solution to the puzzle
def solve_puzzle(puzzle):

    #an array that keeps track of empty entries
    empty = [0,0]

    #if it cant find an entry it'll end the loop
    #a base case
    if (not find_empty(puzzle, empty)):
        return True

    row = empty[0]  #what row the empty entry was in
    col = empty[1]  #what column the empty entry was in

    #runs through numbers 1-9 to test their
    #validity in the empty spot
    for num in range(1,10):

        #if the number is valid then it puts
        #it in that entry
        if (safe_space(puzzle, row, col, num)):
            puzzle[row][col] = num

            #what makes this funtion recursive
            if(solve_puzzle(puzzle)):
                
                #another base case
                return True
            
            #if the number does not work
            #then this resets the value and
            #tries again
            puzzle[row][col] = 0

    #also what makes this function recursive
    return False
