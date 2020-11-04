"""#####################################################################
##                RL Tic Tac Toe - main body                          ##
########################################################################
#   
#   Name: Won Seok Yang
#   
##  Goal is to get two agents to work and learn against each other.
#   This is a smaller problem to solve so I can apply what I learn to
#   the RL Cat and Mouse project.
#
#   The target of each agent is to win the game. Make the move that
#   makes the agent most likely to tie or win the game, prioritizing
#   actions that would lead to eliminating any chance of loss. I do
#   this with the mouse in mind.
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
from board_state import Board
def main():
    myBoard = Board()   # Init empty bpard
    myBoard.display()   #draw board
    print('^ Starting state')

    #keep track of cycles
    #iterate through number of games
    # for _ in range(2):
    #     #reset board
    #     print('\nResetting')
    #     myBoard.resetBoard()
    #     myBoard.display()   #draw board
    #     print('Iteration:', _)

        #while game not over
            #save current game state so agents can manip and revert when they choose an action
            #p1.chooseAction
            #p2.chooseAction
            #
        # while myBoard.winner != 0:
     
    ## Horizontal win test
    # for r in range(3):
    #     for c in range(3):
    #         print('Making a move at %s,%s' % (r,c))
    #         myBoard.placeMove(1, (r,c))
    #         myBoard.display()
    #     print('\nResetting board')
    #     myBoard.resetBoard()
    #  
    ## Vertical win test
    # for r in range(3):
    #     for c in range(3):
    #         print('Making a move at %s,%s' % (c, r))
    #         myBoard.placeMove(2, (c, r))
    #         myBoard.display()
    #     print('\nResetting board')
    #     myBoard.resetBoard()
    #
    ## Diagonal win test
    myBoard.placeMove(3, (0,0))
    myBoard.placeMove(3, (1,1))
    myBoard.placeMove(3, (2,2))
    myBoard.display()
    myBoard.resetBoard()
    #other diagonal
    myBoard.placeMove(4, (0,2))
    myBoard.placeMove(4, (1,1))
    myBoard.placeMove(4, (2,0))
    myBoard.display()


    

    # print(myBoard.board[(0,0)]) #this is actually valid and you can index by tuples

    

    

    

main()