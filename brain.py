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
#   
########################################################################
"""
import pandas as pd
import numpy as np
from consts import ALPHA, GAMMA, EPSILON
import random

class Brain:
    #List of actions provided during first func call
    def __init__(self, player, alpha=ALPHA, gamma=GAMMA, epsilon=EPSILON):
        self.player = player
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        # self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)
    
    # Return <tuple> coord of action to take
    def chooseAction(self, boardState):
        self.state_exist_check(boardState)  #append to q-table if it doesnt exist already
        action = np.random.choice()

    # choose random from list of valid positions
    def randomAction(self, boardState):
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
        randrow = random.randint(0, len(boardState)-1)
        randcol = random.randint(0, len(boardState[0])-1)
        action = (randrow, randcol)
        while boardState[(randrow, randcol)] != 0:
            randrow = random.randint(0, len(boardState)-1)
            randcol = random.randint(0, len(boardState[0])-1)
            action = (randrow, randcol)
        return action

    def printValues(self):
        print(self.__class__.__name__)
        print('self.player=', self.player)
        print('self.alpha=', self.alpha)
        print('self.gamma=', self.gamma)
        print('self.epsilon=', self.epsilon)