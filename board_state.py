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
        #0 for no winner, 1 for p1 winner, 2 for p2 winner, -1 for tie
        self.winner = 0 #holds the winning player
    ## end __init__

    # Place <player> at board[<position>] and return whether or not the game can continue.
    # placeMove(<int>, <tuple>)
    # Return: 
    #   True - there are valid positions left on the board and there is no winner.
    #   False - there are either no valid positions left or a player won.
    def placeMove(self, player, position):
        if self.board[position] == 0:   #only if empty
            self.board[position] = player
            return self.checkWin() #after valid placement, check to see if it's a winning/tie move
        else:
            print('ERROR: invalid placeMove position')
            return False
    ## end placeMove

    def resetBoard(self):
        self.board.fill(0)
        self.winner = 0
    ## end resetBoard

    #this can be optimized by only checking the row, col, and diag of the newly placed move
    # Checks the board for a win or tie state
    # Return:
    #   True - there is a tie or a win
    #   False - the game can continue
    def checkWin(self):
        # Checking rows for win con
        for r in range(len(self.board)):
            x, y, z = self.board[r]
            if x != 0 and x == y and x ==z:
                self.winner = x
                return True
        # Check col for win con
        for row in range(3): #number of elements in a row
            if (self.board[(0, row)] != 0 and 
                self.board[(0, row)] == self.board[(1, row)] and
                self.board[(0, row)] == self.board[(2, row)]):
                self.winner = self.board[(0,row)]
                return True
        # Check diag for win con
        if (self.board[(0,0)] != 0 and
            self.board[(0,0)] == self.board[(1,1)] and
            self.board[(0,0)] == self.board[(2,2)]):
            self.winner = self.board[(0,0)]
            return True
        elif (self.board[(0,2)] != 0 and
            self.board[(0,2)] == self.board[(1,1)] and
            self.board[(0,2)] == self.board[(2,0)]):
            self.winner = self.board[(0,2)]
            return True
        # Check to see if there are still valid empty positions left
        elif 0 in self.board[:,:]:  #there's an empty spot left so game is not over
            return False
        else:   #tie so game over
            self.winner = -1    
            return True
    ## end checkWin

    # Temp text game board so I can work out agent logic in main
    # todo: graphic display instead of terminal print
    def displayBoard(self):
        print('==============')
        print('= Game Board =')
        for _ in self.board:
            print('  ', _)
    ## end displayBoard

    def displayInfo(self):
        print('Winner:', self.winner)
    ## end displayInfo
