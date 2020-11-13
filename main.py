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
    player1 = Brain(1, 'X')   # Player X
    player2 = Brain(-1, 'O')  # Player O

    myBoard.displayBoard()
    myBoard.displayInfo()
    print(player1.printValues())
    print(player2.printValues())
    print('^ Starting state')

    
    print(play(myBoard, player1, player2, 1000))
## end main

# play number of games and save learnings into player1.q_table and player2.q_table
# requires player1 and player2 to be preset before function call
def play(gameboard, player1, player2, number):
    p1win = 0
    p2win = 0
    tiegame = 0
    for _ in range(number):
        print('\nResetting gameboard')
        gameboard.resetBoard()
        print('Iteration:', _)
        
        while True:
            print('\n==ROUND START==')
            print('round start board.winner', gameboard.winner)
            boardState = gameboard.getBoard()
            positions = gameboard.getPositions()
            print('available positions', positions)

            p1action = player1.chooseAction(boardState, positions)
            gameOver = gameboard.placeMove(player1.player, p1action)
            print('Player 1(X) placing in', p1action)
            print('Player 1(X)\'s move result')
            gameboard.displayBoard()

            #Player 2 can only make a move if there are moves left to be played and p1 didnt win
            if not gameOver:
                # print('len(positions)=',len(positions),'myBoard.winner=', myBoard.winner)
                p2action = player2.chooseAction(boardState, positions)
                gameOver = gameboard.placeMove(player2.player, p2action)
                print('Player -1(O) placing in in', p2action)
                print('Player -1(O)\'s move result')
                gameboard.displayBoard()
                # print('After player -1(O)\'s move: len(positions)=',len(positions),'myBoard.winner=', myBoard.winner)            
            
            # No more available positions on the board. Tie.
            if len(positions) == 0 and gameboard.winner == 0:
                print('\nBreaking because the game is a tie.')
                gameboard.displayBoard()
                gameboard.displayInfo()
                print('Tie!')
                # Learn from this iteration of games
                player1.learn(gameboard.winner)
                player2.learn(gameboard.winner)
                tiegame += 1
                break
            # Found a winner
            if gameboard.winner != 0:
                print('\nBreaking because there is a winner.')
                gameboard.displayBoard()
                gameboard.displayInfo()
                print('Player %s won!' % gameboard.winner)
                player1.learn(gameboard.winner)
                player2.learn(gameboard.winner)
                if gameboard.winner==1:
                    p1win += 1
                else:
                    p2win += 1
                break
    gamecount = p1win + p2win + tiegame
    return p1win, p2win, tiegame, gamecount

    # print('p1.q_table', p1.q_table)
    # print('p2.q_table', p2.q_table)
    saveAgent(player1)
    saveAgent(player2)

    # saveAgent(p2)
## end play

# A function to save agent's memory in case I want to use it in the future for testing
def saveAgent(player):
    wfile = csv.DictWriter(open('player'+str(player.name)+'memory.csv', 'w', newline=''), fieldnames=['state', 'action'])
    wfile.writeheader()
    for key,val in player.q_table.items():
        # print('{key:value}', {key:val})
        wfile.writerow({'state' : key,  'action' : val})

def loadAgent(player):
    rfile = csv.DictReader(open('player'+str(player.name)+'memory.csv', 'r'))
    for row in rfile:  
        # print(row)
        # print(row['state'], row['action'])
        player.q_table[row['state']] = row['action']

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

main()
# testingFun()
# test()