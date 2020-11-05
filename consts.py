"""#####################################################################
##                RL Tic Tac Toe - global consts                    ##
########################################################################
#   
#   Name: Won Seok Yang
#   
##  All global 'constant' variables for easy manipulation
#  
########################################################################
##                          Resources                                 ##
########################################################################
#   Style guide:
#   https://www.python.org/dev/peps/pep-0008/#multiline-if-statements
#
########################################################################
"""

# Math values
ALPHA = 0.9             #how heavily the learning algorithm gets changed toward a positive reward (learning rate)
GAMMA = 0.9             #the discount factor of future rewards (0 nearsighted vs 1 farsighted)
EPSILON = 0.9           #the weight of the algo's 'greediness', less greedy = explore, more greedy = exploit

# Reward values:
WIN = 10
LOSE = -10