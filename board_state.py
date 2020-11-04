"""#####################################################################
##                RL Tic Tac Toe - environment                      ##
########################################################################
#   
#   Name: Won Seok Yang
#   
##  Goal is to get two agents to work and learn against each other.
#   This is a smaller problem to solve so I can apply what I learn to
#   the RL Cat and Mouse project.
#
########################################################################
##                          Resources                                 ##
########################################################################
#   Style guide:
#   https://www.python.org/dev/peps/pep-0008/#multiline-if-statements
#   Numpy reference:
#   https://numpy.org/doc/stable/reference/
########################################################################
##                          Notes                                     ##
########################################################################
#   create X and O shapes for easy placement
#   board is a 3x3 array with 0 for empty, 1 for p1, and 2 for p2
########################################################################
"""
from graphics import *
import numpy as np

class Board:
    # Initialize gameboard
    def __init__(self):
        #create a 3x3 2D array with all 0's
        self.board = np.zeros((3,3), dtype='i4')
        #0 for no winner, 1 for p1 winner, 2 for p2 winner
        self.winner = 0 #holds the winning player

    # Place a move and return true or false
    # placeMove(<int>, <tuple>)
    def placeMove(self, player, position):
        if self.board[position] == 0:   #only if empty
            self.board[position] = player
            self.checkWin() #after valid placement, check to see if it's a winning move
            return True
        else:
            return False

    def resetBoard(self):
        self.board.fill(0)
        self.winner = 0
    #redraw

    #this can be optimized by only checking the row, col, and diag of the newly placed move
    # Checks for 3 in a row and updates self.winner with the winning player
    def checkWin(self):
        # Checking horizontally
        for r in range(len(self.board)):
            x, y, z = self.board[r]
            if x != 0 and x == y and x ==z:
                self.winner = x
                break
        # Check vertically
        for row in range(3): #number of elements in a row
            if (self.board[(0, row)] != 0 and 
                self.board[(0, row)] == self.board[(1, row)] and
                self.board[(0, row)] == self.board[(2, row)]):
                self.winner = self.board[(0,row)]
                break
        # Check diagonals
        if (self.board[(0,0)] != 0 and
            self.board[(0,0)] == self.board[(1,1)] and
            self.board[(0,0)] == self.board[(2,2)]):
            self.winner = self.board[(0,0)]
        elif (self.board[(0,2)] != 0 and
            self.board[(0,2)] == self.board[(1,1)] and
            self.board[(0,2)] == self.board[(2,0)]):
            self.winner = self.board[(0,2)]

    # Temp text game board so I can work out agent logic in main
    # todo: graphic display instead of terminal print
    def display(self):
        print('==============')
        print('= Game Board =')
        for _ in self.board:
            print('  ', _)
        print('Winner:', self.winner)
