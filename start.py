#!/usr/bin/python
# Driver program to test above functions 
import searchPath
cost = [[ 0,10, 1, 1, 1],
        [ 1,10, 1, 1, 1],
        [ 1, 1, 1,10, 1],
        [10,10, 1,10, 1],
        [ 1, 1, 1, 1, 1]]
        
maze = [[ 1, 1, 1, 1, 1],
        [ 1,100,100,100, 1],
        [ 1, 0, 100,100, 1],
        [100,100,1,100, 1],
        [ 1, 1, 1, 1, 1]] 
obstacle = 100
path = searchPath.search(maze, 2, 1, 3, 2,obstacle)

"""
https://github.com/calvinfeng/walle_finds_eve
"""