#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import collections
from itertools import combinations
from bisect import bisect


filename = "/Users/vrashabh.irde@carwow.co.uk/Desktop/Advent-of-Code/2023/input.txt" 
grid = []
with open(filename, 'r') as f:
    for line in f:
        grid.append(list(line.strip()))

r,c = len(grid), len(grid[0])

#find # positions
positions = [(i,j) for i in range(c) for j in range(r) if grid[i][j] == '#']
#find rows and columns with gaps
empty_rows = [ i for i in range(c) if all(grid[i][j] == "." for j in range(r))]
empty_col = [ j for j in range(r) if all(grid[i][j] == "." for i in range(c))]


manhattan  = sum(abs(x1-x2)+abs(y1-y2) for (x1,y1),(x2,y2)  in combinations(positions,2))
manhattan_with_gaps = sum(abs(bisect(empty_rows,x1) - bisect(empty_rows, x2)) +
           abs(bisect(empty_col,y1) - bisect(empty_col, y2))
           for (x1,y1),(x2,y2)  in combinations(positions,2))
#part1
print(manhattan + manhattan_with_gaps)
#part2
print(manhattan + manhattan_with_gaps*999999)