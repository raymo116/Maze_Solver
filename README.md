# Maze_Solver
This is a program to solve mazes given an ascii-art layout.

## Usage
```
from maze import Maze
myMaze = Maze()
myMaze.solve()
myMaze.PlotMaze()
```

## Output
![rendered](https://github.com/raymo116/Maze_Solver/blob/master/solved.png?raw=true)

## ASCII Maze Key
Edge: `'X'`

Open: `' '`

Start: `'s'`

End: `'e'`

## Example Maze
```
XsXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X           X   X                      X
X XXXXXXXXX   X   XXXXXXXXXXXXXXXXXXXX X
X X       XXXXXXXXX                    X
X X X XXX           XXXXXXXXXXXXXXXXXX X
X X X  XXXXXXXXXXXXXX     XXX XX XXX   X
X X XX X   X        XX X XX      XXX X X
X X X    X X XXXXXX  X X    XXXXXX   X X
X XXXXXXXX X    X XX   XXXXXXXXXXX XXX X
X      X   XXXX X  XXX           X   X X
XXXXXX XXX X      XXXXXXXXXXXXXX XXX X X
X      X X X XXXX    X   X     X   X X X
X XXXXXX XXX    XXXXXX X XXXX XX XXX X X
X X   X    X XX        X       X   X X X
X X X   X  XX X XXXX XXXXXXXXXXXXX X XXX
X X XXXXXX  X X X    XX     XXXX   X   X
X X      X XX   XXXX    XXX X    XXX X X
X XXXXXX X X  XXX  XXXXXX X X XXXX   XXX
X        X X XX             X      X   X
XXXXXXXXXXXXeXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Rendered
![rendered](https://github.com/raymo116/Maze_Solver/blob/master/unsolved.png?raw=true)

