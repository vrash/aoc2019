#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from math import lcm
import re

mapping = {}
with open("/Users/.../Desktop/Advent-of-Code/2023/input.txt") as f:
    inst, directions = f.read().split("\n\n")
    for ins in directions.split("\n"):
        input, left, right = re.findall("\w\w\w", ins)
        mapping[input] = {
            "L" : left,
            "R" : right
    }

def part1(): 
	steps =0    
	current = 'AAA'
	index = 0
	while current != "ZZZ":
		dir = inst[index]
		current = mapping[current][dir]
		index = (index + 1) % len(inst)
		steps += 1
	print(steps)
    
def part2(): 
    starts = []
    for key, value in mapping.items():
        if key[2] == "A":
            starts.append(key)

    steps = [0 for i in range(0, len(starts))]
    index = 0

    def is_finished(starts):
        for s in starts:
            if s[2] != "Z":
                return False
        return True

    while not is_finished(starts):
        dir = inst[index]
        for i in range(len(starts)):
            if starts[i][2] != "Z":
                starts[i] = mapping[starts[i]][dir]
                steps[i] += 1
        index = (index + 1) % len(inst)
   
    print(lcm(*steps))

part1()
part2()

