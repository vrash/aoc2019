#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import reduce

filename = "/Users/.../Desktop/Advent-of-Code/2023/inputsmall.txt" 
hash = lambda label: reduce(lambda cur, char: (cur + ord(char)) * 17 % 256, label, 0)

with open(filename) as f:
    labels = f.read().split(',')

def part2():
    boxes = defaultdict(dict)

    for label in labels:

        if '-' in label:
            boxes[hash(label[:-1])].pop(label[:-1], None)

        elif '=' in label:
            lens, flength = label.split('=')
            #print(lens, hash(lens))
            boxes[hash(lens)][lens] = int(flength)

    return sum((1+box) * (i+1) * flength for box in boxes for i, flength in enumerate(boxes[box].values()))

part1 = sum(hash(label) for label in labels)
print(part1, part2())