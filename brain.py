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
from consts import ALPHA, GAMMA, EPSILON, WIN, LOSE, TIE
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
            
    # Applies value iteration formula from move history to q_table
    def learn(self, winner):
        if winner == self.player: reward = WIN
        elif winner == 0: reward = TIE
        else: reward = LOSE
        for state in reversed(self.history):
            value = self.q_table.get(state, 0)
            self.q_table.update({state : value})
            #the q-value of the history state in q-table += learning rate * (discount factor*reward - the current value at that state)
            self.q_table[state] += self.alpha * (self.gamma * reward - self.q_table[state])
            #update reward to the q-value of the last move on stack
            reward = self.q_table[state]
        #clear history after learning from it
        self.history.clear()
    ## end learn

    # Choose a random move according to exploration/epsilon chance or
    # from all available positions, make the move with the highest q-value
    def chooseAction(self, boardState, availPositions):
        # Roll to see agent chooses to explore or not
        if np.random.uniform() > self.epsilon:
            action = self.randomAction(boardState, availPositions)
            print('Chose random action')
        else:
            print('inside chooseAction() else:')
            valMax = -999
            # Choose the move with the highest q-value
            for pos in availPositions:
                print('for pos in positions-- pos =', pos)
                boardSim = boardState.copy()
                boardSim[(pos)] = self.player
                boardSimHash = self.convertAndHash(boardSim)
                simQval = self.q_table.get(boardSimHash, 0)  #get q for simulated move
                print('boardState =', boardState)
                print('boardSim =', boardSim)
                print('boardSimHash =', boardSimHash)

                print('before if simQval > valMax:')
                print('simQval=', simQval)
                print('valMax=', valMax)

                if simQval > valMax:
                    valMax = simQval
                    action = pos
                print('before if simQval > valMax:')
                print('simQval=', simQval)
                print('valMax=', valMax)
                print('action=', action)
            self.history.append(self.convertAndHash(boardState))
            print('Outside for loop but still in chooseAction')
            print('action:', action, 'with value', valMax)
            # print(self.q_table)
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
        self.history.append(self.convertAndHash(boardState))
        return action

    def convertAndHash(self, state):
        convert = state.copy()
        # Convert if not player 1
        # # print('convert =',convert)
        # if self.player == -1:
        #     invert = lambda _ : _ *(-1)
        #     convert = invert(convert)
        # #     print('inverted convert =', convert)
        # Return hash
        return str(np.reshape(convert, -1)) #converts to 1d str
    ## end convertAndHash

        """
    # Converts state to a single players perspective and flattens to str to return
    def convertAndHash(self, state):
        # Convert if not player 1
        convert = state.copy()
        print('convert =',convert)
        if self.player == -1:
            invert = lambda _ : _ *(-1)
            convert = invert(convert)
            print('inverted convert =', convert)
        # Return hash
        return str(np.reshape(convert, -1)) #converts to 1d str
    ## end convertAndHash
    """


    # Mainly for testing and troubleshooting
    def printValues(self):
        print(self.__class__.__name__)
        print('self.player=', self.player)
        print('self.alpha=', self.alpha)
        print('self.gamma=', self.gamma)
        print('self.epsilon=', self.epsilon)