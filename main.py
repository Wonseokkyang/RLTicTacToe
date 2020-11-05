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
from brain import Brain
from consts import ALPHA as alpha, GAMMA as gamma, EPSILON as epsilon
from consts import WIN as winReward, LOSE as loseReward



def main():
    myBoard = Board()   # Init empty bpard
    p1 = Brain(1)
    p2 = Brain(2)
    myBoard.displayBoard()   #draw board
    myBoard.displayInfo()

    print('^ Starting state')

    print(p1.printValues())
    print(p2.printValues())


    #keep track of cycles
    # iterate through number of games
    for _ in range(50):
        #reset board
        print('\nResetting')
        myBoard.resetBoard()
        print('Iteration:', _)
     
        #while game not over
            #p1.chooseAction
            #p2.chooseAction
            #
        while True:
            print('\n==ROUND START==')
            print('round start board.winner', myBoard.winner)
            # save current game state so agents can manip and revert when they choose an action
            boardState = myBoard.board

            p1action = p1.randomAction(boardState)
            print('Player 1 placing in', p1action)
            availableMoveLeft = not myBoard.placeMove(1, p1action)

            print('After Player 1\'s move')
            myBoard.displayBoard()

            # print('availableMoveLeft', availableMoveLeft)
            #player 2 can only make a move if p1 didnt tie or win
            if availableMoveLeft == True:
                p2action = p2.randomAction(boardState)
                myBoard.placeMove(2, p2action)
                print('Player 2 placing in in', p2action)

            print('After Player 2\'s move')
            myBoard.displayBoard()

            

            
            if myBoard.winner == -1:
                print('\nBreaking because the game is a tie.')
                myBoard.displayBoard()
                myBoard.displayInfo()
                print('Tie!')
                break;
            if myBoard.winner != 0:
                print('\nBreaking because there is a winner.')
                myBoard.displayBoard()
                myBoard.displayInfo()
                print('Player %s won!' % myBoard.winner)
                break;
            #p1 go
            #check for win
            #p2 go
            #check for win

def test():
    myBoard = Board()   # Init empty bpard
    myBoard.displayBoard()   #draw board
    print('^ Starting state')

    myBoard.placeMove(6, (0,0))
    myBoard.placeMove(6, (0,1))
    myBoard.placeMove(6, (0,2))

    myBoard.placeMove(6, (1,0))
    myBoard.placeMove(6, (1,1))
    myBoard.placeMove(6, (1,2))

    myBoard.placeMove(6, (2,0))
    myBoard.placeMove(6, (2,1))

    myBoard.displayBoard()

    state = myBoard.board

    p1 = Brain()


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
    # myBoard.placeMove(3, (0,0))
    # myBoard.placeMove(3, (1,1))
    # myBoard.placeMove(3, (2,2))
    # myBoard.display()
    # myBoard.resetBoard()
    ##other diagonal
    # myBoard.placeMove(4, (0,2))
    # myBoard.placeMove(4, (1,1))
    # myBoard.placeMove(4, (2,0))
    # myBoard.display()
    

    

main()
# test()