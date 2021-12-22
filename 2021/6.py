import sys
from collections import defaultdict
from collections import defaultdict, Counter
import itertools as it
from copy import deepcopy

with open('/Users/vrashabhirde/Desktop/Advent-Of-Code/2021/input.txt') as f:
    input = list(f.read().split(','))

COUNTER = Counter([int(x) for x in input])

def solve(S, n):
    COUNTER = S
    for i in range(n):
        temp = defaultdict(int)
        for x,count in COUNTER.items():
            if x==0:
                temp[6] += count
                temp[8] += count
            else:
                temp[x-1] += count
        COUNTER = temp
    return sum(COUNTER.values())

#part1
print(solve(COUNTER, 80))
#part2
print(solve(COUNTER, 256))



