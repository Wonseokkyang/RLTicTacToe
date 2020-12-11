"""#####################################################################
##                RL Tic Tac Toe - brain                              ##
########################################################################
#   
#   Name: Won Seok Yang
#   
#   The brain or decision making process of the agent as well as
#   Q-learning function.
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

    def reset(self):
        self.q_table.clear()
        self.history.clear()  
        
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
    # Returns: Action with highest q-value from availPosition param
    def chooseAction(self, boardState, availPositions):
        self.history.append(self.convertAndHash(boardState))

        # Roll to see agent chooses to explore or not
        if np.random.uniform() > self.epsilon:
            actionMax = self.randomAction(boardState, availPositions)
        else:
            valMax = -999
            # Choose the move with the highest q-value
            for pos in availPositions:
                boardSim = boardState.copy()
                boardSim[(pos)] = self.player
                boardSimHash = self.convertAndHash(boardSim)
                simQval = self.q_table.get(boardSimHash, 0)  #get q for simulated move
                self.q_table[boardSimHash] = simQval

                if simQval > valMax:
                    valMax = simQval
                    actionMax = pos
                    boardMax = boardSimHash
            self.history.append(boardMax)
        return actionMax
    ## end chooseAction

    # Choose random from list of valid positions
    # Returns: random valid action
    def randomAction(self, boardState, availPositions):
        #use list of available positions
        action = availPositions[random.randint(0, len(availPositions)-1)]
        self.history.append(self.convertAndHash(boardState))
        return action

    # Deferred converting for future implementation
    # Returns: 1d arr of state parameter
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

    # Mainly for testing and troubleshooting
    def printValues(self):
        print(self.__class__.__name__)
        print('self.player=', self.player)
        print('self.alpha=', self.alpha)
        print('self.gamma=', self.gamma)
        print('self.epsilon=', self.epsilon)
        print('self.q_table=', self.q_table)
        print('self.history=', self.history)