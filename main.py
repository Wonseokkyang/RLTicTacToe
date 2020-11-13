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
#   this with the mouse AI in mind.
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
    print('^ Starting states')

    print('Results: \n P1 win count: %s\n P2 win count: %s\n Tie count: %s\n Total Games: %s' % play(myBoard, player1, player2, 1000))
## end main

# Play number of games and save learnings into player1.q_table 
# and player2.q_table. Requires player1 and player2 to be preset 
# before function call
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
            boardState = gameboard.getBoard()
            positions = gameboard.getPositions()

            p1action = player1.chooseAction(boardState, positions)
            gameOver = gameboard.placeMove(player1.player, p1action)
            print('Player 1(X) placing in', p1action)
            print('Player 1(X)\'s move result')
            gameboard.displayBoard()

            #Player 2 can only make a move if there are moves left to be played and p1 didnt win
            if not gameOver:
                # p2action = player2.randomAction(boardState, positions)
                p2action = player2.chooseAction(boardState, positions)
                gameOver = gameboard.placeMove(player2.player, p2action)
                print('Player -1(O) placing in in', p2action)
                print('Player -1(O)\'s move result')
                gameboard.displayBoard()
            
            # No more available positions on the board. Tie.
            if len(positions) == 0 and gameboard.winner == 0:
                print('\nThe game is a tie.')
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
                print('\nThere is a winner.')
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

    # print('p1.q_table', p1.q_table)
    # print('p2.q_table', p2.q_table)
    saveAgent(player1)
    saveAgent(player2)

    gamecount = p1win + p2win + tiegame
    return p1win, p2win, tiegame, gamecount
    # saveAgent(p2)
## end play

# A function to save agent's memory for future testing
def saveAgent(player):
    wfile = csv.DictWriter(open('player'+str(player.name)+'memory.csv', 
            'w', newline=''), fieldnames=['state', 'action'])
    wfile.writeheader()
    for key,val in player.q_table.items():
        # print('{key:value}', {key:val})
        wfile.writerow({'state' : key,  'action' : val})

# Function to load a saved agent's memory for testing
def loadAgent(player):
    rfile = csv.DictReader(open('player'+str(player.name)+'memory.csv', 'r'))
    for row in rfile:  
        player.q_table[row['state']] = row['action']

main()