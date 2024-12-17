#A*
from collections import defaultdict
import heapq

def parse_grid(input_text):
    grid = []
    start = end = None
    for r, line in enumerate(input_text.splitlines()):
        if line.strip():
            row = list(line)
            if 'S' in row:
                start = (r, row.index('S'))
            if 'E' in row:
                end = (r, row.index('E'))
            grid.append(row)
    return grid, start, end

def get_neighbors(pos, dir, grid):
    r, c = pos
    moves = []
    dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    for new_dir in range(4):
        dr, dc = dirs[new_dir]
        new_r, new_c = r + dr, c + dc
        if (0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] != '#'):
            turn_cost = 1000 if new_dir != dir else 0
            moves.append((new_r, new_c, new_dir, 1 + turn_cost))
    return moves

def find_optimal_paths(grid, start, end):
    pq = [(0, start[0], start[1], 0, {(start[0], start[1])})]
    costs = defaultdict(lambda: float('inf'))
    costs[(start[0], start[1], 0)] = 0
    min_cost = float('inf')
    optimal_tiles = set()
    while pq:
        cost, r, c, dir, path = heapq.heappop(pq)
        if cost > min_cost:
            continue
        if (r, c) == end:
            if cost < min_cost:
                min_cost = cost
                optimal_tiles = path.copy()
            elif cost == min_cost:
                optimal_tiles.update(path)
            continue
        for new_r, new_c, new_dir, move_cost in get_neighbors((r, c), dir, grid):
            new_cost = cost + move_cost
            new_state = (new_r, new_c, new_dir)
            if new_cost <= min_cost and new_cost <= costs[new_state]:
                costs[new_state] = new_cost
                new_path = path | {(new_r, new_c)}
                heapq.heappush(pq, (new_cost, new_r, new_c, new_dir, new_path))
    return min_cost, len(optimal_tiles)

def solve(input_text):
    grid, start, end = parse_grid(input_text)
    min_cost, optimal_tiles = find_optimal_paths(grid, start, end)
    return min_cost, optimal_tiles

with open('/Users/.../Advent-Of-Code/2024/input.txt') as f:
    input_text = f.read()

part1, part2 = solve(input_text)
print(part1)
print(part2)