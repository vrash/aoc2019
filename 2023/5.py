#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re
from collections import defaultdict

part1 = 0
part2 = 0

with open('/Users/vrashabh.irde@carwow.co.uk/Desktop/Advent-of-Code/2023/input.txt') as f:
    inputLines = f.read()

lines = inputLines.split('\n')

for l in lines:
    card = l[8:23]
    mycard = l[25:48]
    internalParts = 0
    first = True
    for win in mycard.split(" "):
        if win!="" and win in card.split(" "):
            if first == True:
                internalParts = 1
                first = False
            else:
                internalParts = internalParts * 2
                print(win, "match", internalParts)
    part1 = part1 + internalParts
              
print (part1)
#print (part2)

