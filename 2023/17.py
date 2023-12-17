#!/usr/bin/python
# -*- coding: utf-8 -*-
import heapq

filename = "/Users/.../Desktop/Advent-of-Code/2023/input.txt" 
GRID = [[ele for ele in row] for row in open(filename).read().strip().split("\n")]
ROWS = len(GRID)
COLS = len(GRID[0])
RIGHT = [0, 1]
DOWN = [1, 0]
LEFT = [0, -1]
UP = [-1, 0]

def Dijk(part1):
  #dijkstra
  PQ = [(0,0,0,-1,-1)]
  GRAPH = {}

  while PQ:
    dist,row,col,direction,fwd_direction = heapq.heappop(PQ)
    if (row,col,direction,fwd_direction) in GRAPH:
      continue
    
    GRAPH[(row,col,direction,fwd_direction)] = dist
    
    for i,(dr,dc) in enumerate([UP,RIGHT,DOWN,LEFT]):
      newrow = row+dr
      newcol = col+dc
      newdirection = i
      newfwddirection = (1 if newdirection!=direction else fwd_direction+1)

      #Up (0) becomes Down (2): (0 + 2) % 4 = 2
      #Right (1) becomes Left (3): (1 + 2) % 4 = 3
      #Down (2) becomes Up (0): (2 + 2) % 4 = 0
      #Left (3) becomes Right (1): (3 + 2) % 4 = 1
      reverse = ((newdirection + 2)%4 == direction)

      if part1:
        isvalidpath = newfwddirection<=3
      else: 
        isvalidpath = newfwddirection<=10 and (newdirection==direction or fwd_direction>=4 or fwd_direction==-1)

      if 0<=newrow<ROWS and 0<=newcol<COLS and not reverse and isvalidpath:
        cost = int(GRID[newrow][newcol])
        heapq.heappush(PQ, (dist+cost, newrow,newcol,newdirection,newfwddirection))

  ans = 1e6
  for (row,col,directon,fwd_direction),v in GRAPH.items():
    if row==ROWS-1 and col==COLS-1:
      ans = min(ans, v)
  return ans

print('Part 1:', Dijk(True))
print('Part 2:', Dijk(False))