#!/usr/bin/python
# -*- coding: utf-8 -*-
filename = "/Users/.../Desktop/Advent-of-Code/2023/input.txt" 

def move(a,b): 
    return ((a[0]+b[0]),(a[1]+b[1]))
def modulus(a): 
    return(a[0]%n, a[1]%n)

grid = open(filename).read().split('\n')
n = len(grid)
assert len(grid) == len(grid[0])

sparse = {(i,j) for i in range(n) for j in range(n) if grid[i][j] in '.S'}
#print("Sparse: ", sparse)
#starting point
S = next((i,j) for i in range(n) for j in range(n) if grid[i][j] == 'S')
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

visited, new, memory = {S}, {S}, {0:1}
assert 26501365%n == n//2

plots_reached_in_cycles, remaining_steps  = 26501365//n, 26501365%n

for c in range(1,remaining_steps+2*n+1): #double steps
    visited = new 
    new = {
    np
    for p in new
    for di in dirs
    for np in [move(p, di)]
    if np not in visited and modulus(np) in sparse
}

    memory[c] = len(new) + (memory[c-2] if c>1 else 0)

diagonal1 = memory[remaining_steps+2*n]-memory[remaining_steps+n]
diagonal2 = memory[remaining_steps+2*n]+memory[remaining_steps]-2*memory[remaining_steps+n]
#part1
print(memory) #answer at position 64
#part2
print(memory[remaining_steps+2*n]+(plots_reached_in_cycles-2)*(2*diagonal1+(plots_reached_in_cycles-1)*diagonal2)//2)


