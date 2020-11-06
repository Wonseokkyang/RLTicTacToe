"""#####################################################################
##                RL Tic Tac Toe - brain                              ##
########################################################################
#   
#   Name: Won Seok Yang
#   
##  
#
########################################################################
##                          Resources                                 ##
########################################################################
#   Style guide:
#   https://www.python.org/dev/peps/pep-0008/#multiline-if-statements
########################################################################
##                          Notes                                     ##
########################################################################
#   What does the q-table look like? The state can be the current state
#   of the board. As for the action, it can be all the non-occupied 
#   spaces left. 
#   ex: 
#   index (?)                       action space(?)
#   state                        (0,0) (0,1) (0,2) (1,0) (1,1) (1,2) (2,0) (2,1) (2,2) 
#   [[0,0,0], [0,0,0], [0,0,0]]   0.0   0.0   0.0   0.0   0.0   0.0   0.5   0.9   1.5
#   [[0,2,0], [1,0,0], [1,2,1]]   0.0   0.0   -10   0.0   10.   -10   0.0   0.0   0.0
#
#   Technically, the player1 and player2 can share the same brain.. 
#   The move you make doesnt depend on if you're 1 or 2 but where your pieces are
#   and where your opponents are. 
#   X| |X                   O| |O  
#    | |O   is the same as   | |X
#    |O|                     |X|
#   So that means convert the state given from the main program to me or not me.
########################################################################
"""
import pandas as pd
import numpy as np
from consts import ALPHA, GAMMA, EPSILON
import random

class Brain:
    #List of actions provided during first func call
    def __init__(self, player, name = '', alpha=ALPHA, gamma=GAMMA, epsilon=EPSILON):
        self.player = player    # player number
        self.name = name        # player's character ('O' | 'X')
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}   # hashed board state : q-value
        self.history = []   # history of moves to update at end of game
    
    # Choose a random move according to exploration/epsilon chance or
    # from all available positions, make the move with the highest q-value
    def chooseAction(self, boardState, availPositions):
        # Roll to see agent chooses to explore or not
        if np.random.uniform() > self.epsilon:
            action = self.randomAction(boardState, availPositions)
        else:
            valMax = -999 #ridiculous negative number works as ceiling value
            # Use dict self. to get q-values of all possible states
            for pos in availPositions:
                boardSim = boardState      #temp board to manip and check q-values
                boardSim[pos] = self.player    #simulating making a move at position pos
                boardSimHash = self.convertAndHash(boardSim)
                simQval = self.q_table.get(boardSimHash, 0)  #get q for simulated move
                #find max of all pos #I think this can be optimized
                if simQval > valMax:
                    valMax = simQval
                    action = pos
        return action
    ## end chooseAction

    # Choose random from list of valid positions
    # Returns: random valid action
    def randomAction(self, boardState, availPositions):
        #something
        # self.state_exist_check(boardState)  #append to q-table if it doesnt exist already
        # validPositions = []
        # for r in range(3):
        #     print('r',r)
        #     temp_row =[]
        #     for c in range(3):
        #         print('c',c)
        #         if boardState[(r,c)] == 0:
        #             temp_row.append(1)
        #         else:
        #             temp_row.append(0)
        #     validPositions.append(temp_row)
        # print('validPositions=', validPositions)

        #pure random
        # randrow = random.randint(0, len(boardState)-1)
        # randcol = random.randint(0, len(boardState[0])-1)
        # action = (randrow, randcol)
        # while boardState[(randrow, randcol)] != 0:
        #     randrow = random.randint(0, len(boardState)-1)
        #     randcol = random.randint(0, len(boardState[0])-1)
        #     action = (randrow, randcol)
        
        #use list of available positions
        action = availPositions[random.randint(0, len(availPositions)-1)]
        print('choose action,', action)
        return action

    # Converts state to a single players perspective and flattens to str to return
    def convertAndHash(self, state):
        # Convert if not player 1
        convert = state
        if self.player == -1:
            invert = lambda _ : _ *(-1)
            convert = invert(convert)
        # Return hash
        return str(convert.resize(9))
    ## end convertAndHash


    def printValues(self):
        print(self.__class__.__name__)
        print('self.player=', self.player)
        print('self.alpha=', self.alpha)
        print('self.gamma=', self.gamma)
        print('self.epsilon=', self.epsilon)