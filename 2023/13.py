#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import defaultdict

filename = "/Users/vrashabh.irde@carwow.co.uk/Desktop/Advent-of-Code/2023/input.txt" 

grid = [[x for x in s.split('\n')if x]for s in open(filename).read().split('\n\n')]
parts = defaultdict(int)
for entry in grid:
    for multiplier, pattern in [(100, entry), (1, list(zip(*entry)))]:
        for i in range(1, len(pattern)):
            p1 = pattern[i:]
            p2 = pattern[:i][::-1]
            differences = sum(c1 != c2 for l1, l2 in zip(p1, p2) for c1, c2 in zip(l1, l2))
            parts[differences] += multiplier * i

print(parts[0]) #no smudge
print(parts[1]) #1 smudge
