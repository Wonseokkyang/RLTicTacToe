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
#   braindump: 
#   should I track the the list of moves made? that way I can back propagate
#   the reward values after the game ends. 
#   Brain: q_table, does the math for q-learning, track previous moves?
#
#   11/6 3:35a
#   program works but there's something wrong with the chooseAction function.
#   it always calculates simQval as 0. must fix when im not so tired.
#   
########################################################################
"""
from board_state import Board
from brain import Brain
from consts import ALPHA as alpha, GAMMA as gamma, EPSILON as epsilon
from consts import WIN as winReward, LOSE as loseReward
import csv


def main():
    myBoard = Board()   # Init empty bpard
    p1 = Brain(1, 'X')   # Player X
    p2 = Brain(-1, 'O')  # Player O

    myBoard.displayBoard()
    myBoard.displayInfo()
    print(p1.printValues())
    print(p2.printValues())
    print('^ Starting state')

    
    # iterate through number of games
    for _ in range(1):
        print('\nResetting')
        myBoard.resetBoard()
        print('Iteration:', _)
        
        while True:
            print('\n==ROUND START==')
            print('round start board.winner', myBoard.winner)
            boardState = myBoard.getBoard()
            positions = myBoard.getPositions()
            print('available positions', positions)

            p1action = p1.chooseAction(boardState, positions)
            gameOver = myBoard.placeMove(p1.player, p1action)
            print('Player 1(X) placing in', p1action)
            print('Player 1(X)\'s move result')
            myBoard.displayBoard()
            # print('After player 1(X)\'s move: len(positions)=',len(positions),'myBoard.winner=', myBoard.winner)

            #Player 2 can only make a move if there are moves left to be played and p1 didnt win
            if not gameOver:
                # print('len(positions)=',len(positions),'myBoard.winner=', myBoard.winner)
                p2action = p2.chooseAction(boardState, positions)
                gameOver = myBoard.placeMove(p2.player, p2action)
                print('Player -1(O) placing in in', p2action)
                print('Player -1(O)\'s move result')
                myBoard.displayBoard()
                # print('After player -1(O)\'s move: len(positions)=',len(positions),'myBoard.winner=', myBoard.winner)            
            
            # No more available positions on the board. Tie.
            if len(positions) == 0 and myBoard.winner == 0:
                print('\nBreaking because the game is a tie.')
                myBoard.displayBoard()
                myBoard.displayInfo()
                print('Tie!')
                # Learn from this iteration of games
                p1.learn(myBoard.winner)
                p2.learn(myBoard.winner)
                break
            # Found a winner
            if myBoard.winner != 0:
                print('\nBreaking because there is a winner.')
                myBoard.displayBoard()
                myBoard.displayInfo()
                print('Player %s won!' % myBoard.winner)
                p1.learn(myBoard.winner)
                p2.learn(myBoard.winner)
                break

    # print('p1.q_table', p1.q_table)
    # print('p2.q_table', p2.q_table)
    saveAgent(p1)
    saveAgent(p2)


# A function to save agent's memory in case I want to use it in the future for testing
def saveAgent(player):
    wfile = csv.DictWriter(open('player'+str(player.name)+'memory.csv', 'w', newline=''), fieldnames=['state', 'action'])
    wfile.writeheader()
    for key,val in player.q_table.items():
        print('{key:value}', {key:val})
        wfile.writerow({'state' : key,  'action' : val})

def loadAgent(player):
    rfile = csv.DictReader(open('player'+str(player.name)+'memory.csv', 'r'))
    for row in rfile:  
        print('row:', row)
        
        # for x, y in row[:-1].split(','):
        #     print('printing row: ', row[:-1])
        #     print(type(row))
            
        #     split_ =row.split(',')
        #     print('printing split_: ', split_)

        # print('printing key, val:', row[0], row[1])
        # kv = {row[0]:row}
        # player.q_table.update({row[0]:row[1]})

def testingFun():
    #testing reading csv into q-table of p1 
    p1 = Brain(1, 'X')
    print('Checking p1.q_table.', p1.q_table)
    loadAgent(p1)

    print('Checking p1.q_table.', p1.q_table)


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
# testingFun()
# test()