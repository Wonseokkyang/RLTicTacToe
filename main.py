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
    p1 = Brain(1, 'X')   # Player X
    p2 = Brain(-1, 'O')  # Player O

    myBoard.displayBoard()   #draw board
    myBoard.displayInfo()
    print(p1.printValues())
    print(p2.printValues())
    print('^ Starting state')



    #keep track of cycles
    # iterate through number of games
    for _ in range(1):
        #reset board
        print('\nResetting')
        myBoard.resetBoard()
        print('Iteration:', _)


        while True:
            print('\n==ROUND START==')
            print('round start board.winner', myBoard.winner)
            # save current game state so agents can manip and revert when they choose an action
            boardState = myBoard.getBoard()
            positions = myBoard.getPositions()

            ## replacing this with p1.chooseAction
            p1action = p1.randomAction(boardState, positions)
            gameOver = myBoard.placeMove(p1.player, p1action)
            print('Player 1(X) placing in', p1action)
            print('Player 1(X)\'s move result')
            myBoard.displayBoard()
            ##
            
            # p1action =p1.chooseAction(boardState, positions)
            # gameOver = myBoard.placeMove(p1.player, p1action)
            #

            print('After player 1(X)\'s move: len(positions)=',len(positions),'myBoard.winner=', myBoard.winner)


            #Player 2 can only make a move if there are moves left to be played and p1 didnt win
            if not gameOver:
                print('len(positions)=',len(positions),'myBoard.winner=', myBoard.winner)
                p2action = p2.randomAction(boardState, positions)
                gameOver = myBoard.placeMove(p2.player, p2action)
                print('Player -1(O) placing in in', p2action)
                print('Player -1(O)\'s move result')
                myBoard.displayBoard()
                print('After player -1(O)\'s move: len(positions)=',len(positions),'myBoard.winner=', myBoard.winner)            
            
            # No more available positions on the board. Tie.
            if len(positions) == 0 and myBoard.winner == 0:
                print('\nBreaking because the game is a tie.')
                myBoard.displayBoard()
                myBoard.displayInfo()
                print('Tie!')
                break;

            # Found a winner
            if myBoard.winner != 0:
                print('\nBreaking because there is a winner.')
                myBoard.displayBoard()
                myBoard.displayInfo()
                print('Player %s won!' % myBoard.winner)
                break;

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