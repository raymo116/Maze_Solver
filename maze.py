import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
'''
This class defines a maze object that is designed based on ascii art in a given filepath
The key for the maze is as follows:
- Edge: 'X'
- Open: ' '
- Start: 's'
- End: 'e'
'''
class Maze:
    # Tile types
    visited = -1
    space = 0
    wall = 1
    end = 2
    path = 3


    '''
    Initializes an empty maze
    '''
    def __init__(self):
        # Maze itself
        self.maze = []
        # Starting coordinates
        self.start = []
        # Colormap for maze display
        self.cm = LinearSegmentedColormap.from_list(
        "co", [(1,1,1), (1,1,1), (0,0,0), (0,0,1), (0,1,0)])

    '''
    Initializes a maze built from ascii art
    Takes in an optional filepath, defaulted to ./maze.txt
    '''
    def __init__(self, fp = "./maze.txt"):
        self.maze, self.start = self.convertFromAsciiToMaze(fp)
        self.cm = LinearSegmentedColormap.from_list(
        "co", [(1,1,1), (1,1,1), (0,0,0), (0,0,1), (0,1,0)])

    '''
    Creates a maze out of ascii art given a filepath
    '''
    def convertFromAsciiToMaze(self, fp: str):
        # String input from file
        i = ""
        with open(fp) as f:
            i = f.readlines()


        maze = []
        # Coordinates
        begining = []

        # Cycle through the string and assign all values
        for line in range(len(i)):
            k = []
            for char in range(len(i[line])):
                if(i[line][char] == 'X'):
                    k.append(Maze.wall)
                elif(i[line][char] == 's'):
                    begining = [line, char]
                    k.append(Maze.space)
                elif(i[line][char] == 'e'):
                    end = [line, char]
                    k.append(Maze.end)
                elif(i[line][char] == ' '):
                    k.append(Maze.space)
            if(len(k)):
                maze.append(k)

        # Return the maze and the begining
        return np.array(maze), begining

    '''
    Defines the recursive movement through the maze
    '''
    def __move(self, m, y, x):
        # If the given space is a wall or a previously-visited position
        if((m[y][x] == Maze.wall) or (m[y][x] == Maze.visited)):
            return False

        # If the given space is not the end
        if(m[y][x] != Maze.end):
            # Mark as visited
            m[y][x] = Maze.visited

            # See if any of the paths return true
            b = (self.__move(m, y+1, x) or self.__move(m, y, x-1) or self.__move(m, y-1, x) or self.__move(m, y, x+1))

            # If one does, mark this as the correct path
            if(b):
                m[y][x] = Maze.path
            return b

        # If the maze is solved
        if(m[y][x] == Maze.end):
            # mark as the correct path and return
            m[y][x] = Maze.path
            return True

    '''
    Solves the maze by calling the recursive "move" function
    '''
    def solve(self):
        self.__move(self.maze, self.start[0], self.start[1])

    '''
    Displays the maze in its current standing
    '''
    def PlotMaze(self):
        plt.imshow(self.maze, cmap=self.cm,  interpolation='nearest')
        plt.xticks([], [])
        plt.yticks([], [])
        plt.plot()
