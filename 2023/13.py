#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import defaultdict

filename = "/Users/.../Desktop/Advent-of-Code/2023/input.txt" 

grid = [[x for x in s.split('\n')if x]for s in open(filename).read().split('\n\n')]
parts = defaultdict(int)
for entry in grid:
     #loop across grid and transpose of grid, using multiplier tuples
    for multiplier, pattern in [(100, entry), (1, list(zip(*entry)))]:
        for i in range(1, len(pattern)):
            #next line
            below_or_right = pattern[i:]
            
            #previous line reversed
            above_or_left = pattern[:i][::-1]
            
            #find how many characters are different between the two and add to dict
            differences = sum(c1 != c2 for l1, l2 in zip(below_or_right, above_or_left) for c1, c2 in zip(l1, l2))
            
            #build dictionary of differences with rules multiplier i.e. 100 for horizontal and 1 for vertical (transposed)
            parts[differences] += multiplier * i

print(parts[0]) #no smudge i.e. no differences found
print(parts[1]) #1 smudge i.e. for 1 difference
