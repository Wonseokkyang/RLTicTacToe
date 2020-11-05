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
        self.player = player
        self.name = name
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        # self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)
    
    # Return <tuple> coord of action to take
    def chooseAction(self, boardState):
        self.state_exist_check(boardState)  #append to q-table if it doesnt exist already
        action = np.random.choice()

    # choose random from list of valid positions
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

    def printValues(self):
        print(self.__class__.__name__)
        print('self.player=', self.player)
        print('self.alpha=', self.alpha)
        print('self.gamma=', self.gamma)
        print('self.epsilon=', self.epsilon)