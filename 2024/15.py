from dataclasses import dataclass
from typing import List, Set, Tuple

def parse_input(input_text: str) -> Tuple[List[List[str]], List[str]]:
    parts = input_text.strip().split('\n\n')
    grid = [list(line) for line in parts[0].splitlines() if line.strip()]
    moves = ''
    for line in parts[1].splitlines():
        moves += line.strip()
    return grid, list(moves)

def find_robot(grid: List[List[str]]) -> Tuple[int, int]:
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@':
                return r, c
    return -1, -1

def try_move(grid: List[List[str]], robot_pos: Tuple[int, int], dir: str) -> Tuple[int, int]:
    r, c = robot_pos
    dr = dc = 0
    if dir == '^': dr = -1
    elif dir == 'v': dr = 1
    elif dir == '<': dc = -1
    elif dir == '>': dc = 1
    new_r, new_c = r + dr, c + dc
    if grid[new_r][new_c] == '#':
        return r, c
    if grid[new_r][new_c] == '.':
        grid[r][c] = '.'
        grid[new_r][new_c] = '@'
        return new_r, new_c
    if grid[new_r][new_c] == 'O':
        box_new_r, box_new_c = new_r + dr, new_c + dc
        if grid[box_new_r][box_new_c] in '#O':
            return r, c
        grid[box_new_r][box_new_c] = 'O'
        grid[new_r][new_c] = '@'
        grid[r][c] = '.'
        return new_r, new_c
    return r, c

def calculate_gps(grid: List[List[str]]) -> int:
    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'O':
                total += (100 * r + c)
    return total

def simulate(grid: List[List[str]], moves: List[str]) -> int:
    robot_pos = find_robot(grid)
    for move in moves:
        robot_pos = try_move(grid, robot_pos, move)
    return calculate_gps(grid)

def solve(input_text: str) -> int:
    grid, moves = parse_input(input_text)
    return simulate(grid, moves)

with open('/Users/.../Advent-Of-Code/2024/input.txt') as f:
    input_text = f.read()

print(solve(input_text))