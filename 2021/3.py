
import itertools as it
from copy import deepcopy

with open('/Users/vrashabhirde/Desktop/Advent-Of-Code/2021/input.txt') as f:
    input = list(f.read().splitlines())

A0 = {}
A1 = {}

def part1():
    gamma = ''
    epsilon = ''
    for x in input:
        for i,c in enumerate(x):
            if i not in A0:
                A0[i] = 0;
            if i not in A1:
                A1[i] = 0; 
            if c == '1':
                A1[i] += 1
            elif c == '0':
                A0[i] += 1

    
    for i in A0:
        if A0[i] > A1[i]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    print(int(gamma,2) * int(epsilon,2))
        
part1()
