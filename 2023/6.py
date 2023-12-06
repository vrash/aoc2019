#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict
import math
from math import prod

with open('/Users/.../Desktop/Advent-of-Code/2023/input.txt') as f:  # Replace with your actual file path
    times, distance = [[int(x) for x in line.split(':')[1].split()] for line in f.read().split('\n')[:2]]

#et tu brute
def f(t, d):
    return sum(1 for x in range(t + 1) if x * (t - x) >= d)
T, D = int(''.join(map(str, times))), int(''.join(map(str, distance)))
print(f(T, D), prod(f(t, d) for t, d in zip(times, distance)))

bhaskara_time = [int(''.join(map(str, times)))]
bhaskara_distance = [int(''.join(map(str, distance)))]

#bhaskara 
def bhaskara(times,distance):
    result = 1
    #print(times)
    for i in range(len(times)):
        b = times[i]
        c = distance[i]
        delta = math.sqrt(b*b -4*c)
        minR = math.floor(((b-delta)/2) +1)
        maxR = math.ceil(((b+delta)/2)-1)
        diff = maxR-minR+1
        result = result * diff
    print(result)
#part1
bhaskara(times,distance)
#part2 
bhaskara(bhaskara_time,bhaskara_distance)