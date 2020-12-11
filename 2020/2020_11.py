import itertools as it
from copy import deepcopy

with open('/Users/vrashabhirde/Desktop/aoc1/input.txt') as f:
    input = list(map(list, f.read().splitlines()))

R, C = len(input), len(input[0])

def isvalid(r, c): #bounds check
    return 0 <= r <R and 0 <= c < C
    
def alladjacentneighbours(r, c): #all neighbours check
    return [(r-1, c-1), (r-1, c+1), (r, c-1), (r+1, c),
            (r+1, c+1), (r+1, c-1), (r, c+1), (r-1, c)]


def visibleneighbours(r, c):
    vibileneighbours = []
    for rc, cc in alladjacentneighbours(0, 0):
        for k in it.count(1):
            row = r + k * rc
            col = c + k * cc
            if isvalid(row, col):
                if grid[row][col] != '.':
                    vibileneighbours.append((row, col))
                    break
            else:
                break
    return vibileneighbours


for neighbours, vibileneighbours in [(alladjacentneighbours, 4), (visibleneighbours, 5)]:
    grid = input
    for e in it.count():
        gridcopy = deepcopy(grid)

        for i, row in enumerate(grid):
            for j, seat in enumerate(row):

                if seat == 'L' and all(grid[x][y] != '#'
                                       for x, y in neighbours(i, j)
                                       if isvalid(x, y)):
                    gridcopy[i][j] = '#'

                elif seat == '#' and sum(grid[x][y] == '#'
                                         for x, y in neighbours(i, j)
                                         if isvalid(x, y)) >= vibileneighbours:
                    gridcopy[i][j] = 'L'


        if grid == gridcopy: 
            print(sum(c == '#' for row in gridcopy for c in row))
            break

        grid = gridcopy

