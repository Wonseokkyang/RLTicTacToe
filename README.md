# Reinforced Learning - Tic-Tac-Toe
Author: Chase (Won Seok) Yang <br/>

![alt text](https://github.com/Wonseokkyang/RLTicTacToe/blob/master/results/demo.gif?raw=true)

A *dual* reinforced learning project in the form of a game of Tic-Tac-Toe.

In this project there are two agents who compete against one another. After completing my first reinforced learning agent with Python in my [Maze](https://github.com/Wonseokkyang/RLMaze) project, I brought my learnings with me to tackle the problem of a dual agent problem.

Unlike the maze project, the state space of the environment is considerably smaller. Both agents inherit their learning algorithm from the same base class but have different q-tables to hold their experiences. Similar to the maze learning agent, the Tic-Tac-Toe agents have alpha, gamma and epsilon values that they use in their learning algorithm.
```
# Math values
ALPHA = 0.9     #how heavily the learning algorithm gets changed toward a positive reward (learning rate)
GAMMA = 0.9     #the discount factor of future rewards (0 nearsighted vs 1 farsighted)
EPSILON = 0.9     #the weight of the algo's 'greediness', less greedy = explore, more greedy = exploit

# Reward values:
WIN = 10
LOSE = -10
TIE = -1
```
### Example q-table of agent:
![alt text](https://github.com/Wonseokkyang/RLTicTacToe/blob/master/results/q_table.jpeg?raw=true)

Although these agents are similar to the maze agent, these agents have some large differences. Instead of a state:action(s) tuple, they use state:value tuple. The state in this case, is a hashed version of the board environment and value amount represents how 'good' it is for the agent to be in that state.

At every turn, the agent checks every action it can take from that state and evaluates the value of the resulting possible future states.
Once a game is completed, due to a tie or win condition, these agents receive a reward/penalty and use backpropagation to update previously visted states according to their tracked history. Moves/states closer to the end receive a higher weight and the further states receive a lower weight.

### Findings:
After implementing the environment and agent interaction, I tested a run of 1,000 and 10,000 games played between the two agents.
#
```
alpha:      0.9
gamma:      0.9
epsilon:    0.9
```
![alt text](https://github.com/Wonseokkyang/RLTicTacToe/blob/master/results/1000_e%3D9.jpg?raw=true)
![alt text](https://github.com/Wonseokkyang/RLTicTacToe/blob/master/results/10000_e%3D9.jpg?raw=true)
#
```
alpha:      0.9
gamma:      0.9
epsilon:    1.0
```
![alt text](https://github.com/Wonseokkyang/RLTicTacToe/blob/master/results/result_1000.jpeg?raw=true)
![alt text](https://github.com/Wonseokkyang/RLTicTacToe/blob/master/results/result_10000.jpeg?raw=true)
#
The above tests show the dramatic effect of a 0.1 value difference in epsilon value- an agent with an epsilon value of 1.0 always choosing best possible action.
I can conclude from these tests that the first player to make a move has a definitive advantage over the player who goes second.

This project was just a stepping stone to figure out how to implement a larger project that incorporates both environment exploration from the [Maze project](https://github.com/Wonseokkyang/RLMaze) as well as reactionary decision making process learned in this project. 

The result will be a dual agent, reinforced learning [Cat and Mouse](https://github.com/Wonseokkyang/RLCatMouse) program.

## Libraries used:
csv - for saving/loading agent's q-value table for testing purposes <br/>
```pip install csv```

numpy - used for storage and array search/manipulation in agent's value table <br/>
```pip install numpy```

random - for seleting a random action from pool of actions with equivalent q-values <br/>
```pip install random```


