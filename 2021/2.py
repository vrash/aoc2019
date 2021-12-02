
import itertools as it
from copy import deepcopy

with open('/Users/vrashabhirde/Desktop/Advent-Of-Code/2021/input.txt') as f:
    input = list(x.split() for x in f.read().splitlines())

print (input)


def part1():
    hor = 0
    depth = 0

    for x,y in input:
        if x=='forward':
            hor= hor+ int(y)
        elif x=='up':
            depth = depth - int(y)
        elif x=='down':
            depth = depth + int(y)
    print (hor * depth)


def part2():
    hor = 0
    depth = 0
    aim = 0
    for x,y in input:
        if x=='forward':
            hor= hor+ int(y)
            depth = depth + (aim * int(y))
        elif x=='up':
            aim = aim - int(y)
            #depth = depth - int(y)
        elif x=='down':
            aim = aim + int(y)
            #depth = depth + int(y)
    print (hor * depth)


part1()    
part2()
