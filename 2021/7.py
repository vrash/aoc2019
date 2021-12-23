import sys
from collections import defaultdict
from collections import defaultdict, Counter
import itertools as it
from copy import deepcopy

with open('/Users/vrashabhirde/Desktop/Advent-Of-Code/2021/input.txt') as f:
    input = list(f.read().strip().split(','))

INPUT = [int(x) for x in input]

#part 1
def part1():
    INPUT.sort()
    #print (INPUT)
    ans = 0
    median = INPUT[len(INPUT)//2]
    for x in INPUT:
        ans += abs(x-median)
    print (ans)

#part 2 - based on an idea from the official reddit thread
def part2(): 
    ans = 1e9
    for median in range(5000): 
        score = 0
        for x in INPUT:
            d = abs(x-median)
            score += d*(d+1)/2
        if score < ans:
            ans = score
    print (ans)

part1()
part2()
