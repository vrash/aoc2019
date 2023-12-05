#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re
from collections import defaultdict


part1 = 0
part2 = 0
Numbers = defaultdict(int)

with open('/Users/.../Desktop/Advent-of-Code/2023/input.txt') as f:  # Replace with your actual file path
    lines = f.read().split('\n')


for i,line in enumerate(lines):
    Numbers[i] += 1
    if '|' in line:
        first, second = line.split('|')
        card_id_, card = first.split(':')
        ticket = set(map(int, card.split()))
        mycard = set(map(int, second.split()))
        val = len(ticket & mycard)
  
        if val > 0:
            part1 += 2**(val-1)

        for j in range(val):
            Numbers[i+1+j] += Numbers[i]
part2 = sum(Numbers.values())

print(part1)
print(part2)