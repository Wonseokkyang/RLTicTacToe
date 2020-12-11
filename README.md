# Reinforced Learning - Tic-Tac-Toe
Author: Chase (Won Seok) Yang <br/>

![alt text](https://github.com/Wonseokkyang/RLTicTacToe/blob/master/results/demo.gif?raw=true)

A *dual* reinforced learning project in the form of a game of Tic-Tac-Toe.

In this project there are two agents who compete against one another. After completing my first reinforced learning agent with Python in my [Maze](https://github.com/Wonseokkyang/RLMaze) project, I brought my learnings with me to tackle the problem of a dual agent problem.

Unlike the maze project, the state space of the environment is considerably smaller. Both agents inherit their learning algorithm from the same base class but have different q-tables to hold their experiences. Similar to the maze learning agent, the Tic-Tac-Toe agents have alpha, gamma and epsilon values they use in their learning algorithm.
```
# Math values
ALPHA = 0.9     #how heavily the learning algorithm gets changed toward a positive reward (learning rate)
GAMMA = 0.9     #the discount factor of future rewards (0 nearsighted vs 1 farsighted)
EPSILON = 1     #the weight of the algo's 'greediness', less greedy = explore, more greedy = exploit

# Reward values:
WIN = 10
LOSE = -10
TIE = -1
```



Description(Describe by words and images alike)
Demo(Images, Video links, Live Demo links)
Technologies Used
Special Gotchas of your projects (Problems you faced, unique elements of your project)
Technical Description of your project like- Installation, Setup, How to contribute.

Project description
<image>

<gif>

