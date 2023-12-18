#!/usr/bin/python
# -*- coding: utf-8 -*-
filename = "/Users/.../Desktop/Advent-of-Code/2023/input.txt" 

dirs = {"U": (-1,0), "D":(1,0), "L": (0,-1), "R": (0,1)}

def solve(part1):
  grid = [(0,0)]
  boundarypoints = 0
  for line in open(filename):
    d,n,col = line.strip().split(" ")
    col = col[2:-1]
    if part1:
      dr,dc = dirs[d]
      n = int(n)
    else:
      dr,dc = dirs["RDLU"[int(col[-1])]]
      n = int(col[:-1], 16)
    r,c = grid[-1]
    boundarypoints += n
    #print(boundarypoints)
    grid.append((r+ dr* n, c+dc* n))
  
  return(area(grid, boundarypoints))

def area(grid, boundarypoints):  
  #shoelace formula - https://en.wikipedia.org/wiki/Shoelace_formula#:~:text=The%20shoelace%20formula%2C%20also%20known,Cartesian%20coordinates%20in%20the%20plane.
  A = abs(sum(grid[i][0] * (grid[i-1][1]-grid[(i+1) %len(grid)][1]) for i in range(len(grid))))/2
   
  #picks theorem - https://en.wikipedia.org/wiki/Pick%27s_theorem 
  i = A-boundarypoints//2+1
  return(i + boundarypoints)

print("Part 1:", solve(True))
print("Part 2:", solve(False))