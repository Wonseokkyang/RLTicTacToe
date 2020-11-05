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
#   board is a 3x3 array with 
#       0 = empty space
#       1 = player 1
#       -1 = player2
#   ========================
#   last working on adding available spots to board for brain
#   ==============
#
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
        self.setPositions()
        #has self.position = []
    ## end __init__

    # Place <player> at board[<position>] and return whether or not the game is over.
    # placeMove(<int>, <tuple>)
    # Return: 
    #   True - there are valid positions left on the board and there is no winner.
    #   False - there are either no valid positions left or a player won.
    def placeMove(self, player, position):
        if self.board[position] != 0:
            raise Exception('ERROR: invalid placeMove(player, position) position.')
            exit()
        elif self.board[position] == 0: #only if empty
            self.board[position] = player
            #remove that position from self.positions
            self.positions.remove(position)
            return self.checkGameOver() #after valid placement, check to see if it's a winning/tie move
        else:
            print('MESSAGE: this should never print.')
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
    def checkGameOver(self):
        # Checking rows for win con
        for r in range(len(self.board)):
            x, y, z = self.board[r]
            if x != 0 and x == y and x ==z:
                self.winner = x
                return True
        # Check col for win con
        for col in range(3): #number of elements in a row
            if (self.board[(0, col)] != 0 and 
                self.board[(0, col)] == self.board[(1, col)] and
                self.board[(0, col)] == self.board[(2, col)]):
                self.winner = self.board[(0,col)]
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
        # Check for tie
        if len(self.positions) == 0:  #No more spots so game over
            return True
        else:   # Not a tie so game not over
            return False
    ## end checkGameOver

    #optimization oportunity. it's only called once so initialize a list of
    # Check self.board and get all available/empty spaces
    def setPositions(self):
        positions = []
        for x in range(3):
            for y in range(3):
                if self.board[(x,y)] == 0:
                    positions.append((x,y))
        self.positions = positions
    ## end setPositions

    # Return: list of available positions
    def getPositions(self):
        return self.positions
    ## end getPositions

    def getBoard(self):
        return self.board
    ## end getBoard
        
    # Temp text game board so I can work out agent logic in main
    # todo: graphic display instead of terminal print
    def displayBoard(self):
        print('==============')
        print('= Game Board =')
        # for row in self.board:
        #     print('  ', row)
        for row in self.board:
            toPrint = ' | '
            for col in row:
                if col == 1: 
                    toPrint += 'X'
                elif col == -1: 
                    toPrint +=  'O'
                else:
                    toPrint += ' '
                toPrint += ' | '
            print(toPrint)

    ## end displayBoard

    def displayInfo(self):
        print('Winner:', self.winner)
    ## end displayInfo
