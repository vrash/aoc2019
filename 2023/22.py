#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import deque
filename = "/Users/..../Desktop/Advent-of-Code/2023/input.txt" 

bricks = [list(map(int,line.replace("~",",").split(","))) for line in open(filename)]

#x ranges and y ranges intersect then bricks overlap 
def overlap(a,b):
    return max(a[0],b[0])<= min(a[3],b[3]) and max(a[1],b[1])<=min(a[4],b[4])

#sort by z-value
bricks.sort(key=lambda brick:brick[2])

#simulate falling
for index, brick in enumerate(bricks):
    max_z = 1
    for check in bricks[:index]:
        if overlap(brick,check):
            max_z = max(max_z,check[5] + 1)
    brick[5] -= brick[2] - max_z
    brick[2] = max_z
bricks.sort(key=lambda brick:brick[2])
#print(bricks)

#all k supports v, and all v supports k
k_v = {i:set() for i in range(len(bricks))}
v_k = {i:set() for i in range(len(bricks))}

for j, higher in enumerate(bricks):
    for i, lower in enumerate(bricks[:j]):
        #lower supports higher brick
        if overlap(lower,higher) and higher[2]==lower[5]+1:
            k_v[i].add(j)
            v_k[j].add(i)
#print(v_k)
#print(k_v)

def part1():
    total = 0
    for i in range(len(bricks)):
        if all(len(v_k[j])>=2 for j in k_v[i]):
            total = total + 1
    print(total)

def part2():
    total = 0
    for i in range(len(bricks)):
        q = deque(j for j in k_v[i] if len(v_k[j])==1)
        falling = set(q)
        falling.add(i)
        while q:
            j = q.popleft()
            for k in k_v[j] - falling:
                if v_k[k]<= falling:
                    q.append(k)
                    falling.add(k)
        total = total + len(falling) -1 
    print(total)


part1()
part2()