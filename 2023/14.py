#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import defaultdict

filename = "/Users/.../Desktop/Advent-of-Code/2023/input.txt" 
with open(filename, 'r') as f:
    inputpattern = f.read()

grid = [list(row) for row in inputpattern.split('\n')]
rows, cols = len(grid), len(grid[0])

def news(grid, row, col,part2):
        for c in range(col):
            lim = 0
            for r in range(row):
                if grid[r][c] == '#':
                    lim = r + 1
                elif grid[r][c] == 'O':
                    if r > lim:
                        grid[lim][c] = 'O'
                        grid[r][c] = '.'
                    lim += 1
        if(part2):
            for r in range(row):
                lim = 0
                for c in range(col):
                    if grid[r][c] == '#':
                        lim = c + 1
                    elif grid[r][c] == 'O':
                        if c > lim:
                            grid[r][lim] = 'O'
                            grid[r][c] = '.'
                        lim += 1
            for c in range(col):
                lim = row - 1
                for r in reversed(range(row)):
                    if grid[r][c] == '#':
                        lim = r - 1
                    elif grid[r][c] == 'O':
                        if r < lim:
                            grid[lim][c] = 'O'
                            grid[r][c] = '.'
                        lim -= 1
            for r in range(row):
                lim = col - 1
                for c in reversed(range(col)):
                    if grid[r][c] == '#':
                        lim = c - 1
                    elif grid[r][c] == 'O':
                        if c < lim:
                            grid[r][lim] = 'O'
                            grid[r][c] = '.'
                        lim -= 1
        return sum((grid[r][c]=='O') * (rows-r) for r in range(rows) for c in range(cols))  

def part1(inputpattern):
    return(news(grid,rows,cols,False))
    

def part2(inputpattern):
    cache = {}
    loads = []
    for i in range(300):
        loads.append(news(grid,rows,cols,True))
        if i > 20:
            state = str(loads[-20:])
            if state in cache:
                start = cache[state]
                length = i - start
                break
            cache[state] = i

    target = 1_000_000_000
    delta = (target - start) % length - 1  
    return loads[start + delta]

print('Part 1:', part1(inputpattern))
print('Part 2:', part2(inputpattern))

