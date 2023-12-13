#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from functools import cache


filename = "/Users/vrashabh.irde@carwow.co.uk/Desktop/Advent-of-Code/2023/input.txt" 

grid = []
with open(filename, 'r') as f:
    for line in f:
        grid.append(line.split())

part1, part2 = {}, {}



def transform(entries, springs, res = 0):

    if not springs:
        return '#' not in entries
    curr, springs = springs[0], springs[1:]
    #print(curr,springs)
    for i in range(len(entries)-sum(springs)-len(springs)-curr+1):
        if '#' in entries[:i]:
            break
        if(nxt := i+ curr)<=len(entries) and '.' not in entries[i:nxt] and entries[nxt:nxt + 1] !="#":
            res += transform(entries[nxt + 1:], springs)
    return res

#print(grid)
for e, (entries,springs) in enumerate(grid):
    #print(e, entries, springs)

    part1[e] = transform(entries, (springs := tuple(map(int,springs.split(",")))))
    part2[e] = transform("?".join([entries] * 5), springs * 5)

#part1 
print(sum(x for x in part1.values()))
#part2
print(sum(x for x in part2.values()))


