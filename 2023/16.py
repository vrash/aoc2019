#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import deque


filename = "/Users/.../Desktop/Advent-of-Code/2023/input.txt" 
GRID = open(filename).read().strip().split()

RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
UP = (-1, 0)
ROWS = len(GRID)
COLS = len(GRID[0])

def energize(beam):
    setofenergizedpoints = set()
    beams = [beam]

    while any(beams):
        for i, beam in enumerate(beams):
            if not beam:
                continue
            (x, y), (dx, dy) = beam
            if beam in setofenergizedpoints:
                beams[i] = None
            else:
                setofenergizedpoints.add(beam)
                x += dx
                y += dy
                if min(x, y) < 0 or y >= ROWS or x >= COLS:
                    beams[i] = None
                    continue
                cell = GRID[y][x]
                if cell == '/':
                    dx, dy = -dy, -dx
                elif cell == '\\':
                    dx, dy = dy, dx
                elif cell == '-' and dy:
                    dx, dy = DOWN
                    beams.append(((x, y), (UP)))
                elif cell == '|' and dx:
                    dx, dy = RIGHT
                    beams.append(((x, y), (LEFT)))
                beams[i] = (x, y), (dx, dy)

    return len({point for point, _ in setofenergizedpoints}) - 1

part1_beam = (UP,DOWN)
print('Part 1:', energize(part1_beam))


print('Part 2:', max([
    *(energize(((i, -1), (RIGHT))) for i in range(COLS)),
    *(energize(((i, ROWS), (LEFT))) for i in range(COLS)),
    *(energize(((-1, i), (DOWN))) for i in range(ROWS)),
    *(energize(((COLS, i), (UP))) for i in range(ROWS))
]))