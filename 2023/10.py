#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import collections
from queue import Queue

filename = "/Users/.../Desktop/Advent-of-Code/2023/inputsmall.txt" 
def read_grid_from_file(filename):
    with open(filename, 'r') as f:
        grid = []
        for line in f:
            grid.append(line.strip())
    return grid

def print_queue(q):
    temp_list = []
    print("Queue contents:")
    while not q.empty():
        item = q.get()
        print(item)
        temp_list.append(item)

    # Re-queue the items
    for item in temp_list:
        q.put(item)

def find_max_distance(grid):
    directions = {
        "|": [(0, -1), (0, 1)],
        "-": [(-1, 0), (1, 0)],
        "L": [(0, -1), (1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(-1, 0), (0, 1)],
        "F": [(1, 0), (0, 1)],
    }
    start_x = start_y = None
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "S":
                start_x, start_y = x, y
                break
        if start_x is not None:
            break


    q = Queue()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        c = grid[start_y + dy][start_x + dx]
        if c in directions:
            for dx2, dy2 in directions[c]:
                if start_x == start_x + dx + dx2 and start_y == start_y + dy + dy2:
                    q.put((1, (start_x + dx, start_y + dy)))

    print_queue(q)

    dists = {(start_x, start_y): 0}
    assert q.qsize() == 2
    
    while not q.empty():
        d, (x, y) = q.get()

        if (x, y) in dists:
            continue

        dists[(x, y)] = d

        for dx, dy in directions[grid[y][x]]:
            q.put((d + 1, (x + dx, y + dy)))

    return max(dists.values())

print(find_max_distance(read_grid_from_file(filename)))



