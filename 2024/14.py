from collections import defaultdict
import re
from statistics import median

def parse_input(input_text):
    robots = []
    pattern = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
    for line in input_text.splitlines():
        if line.strip():
            x, y, dx, dy = map(int, re.match(pattern, line).groups())
            robots.append((x, y, dx, dy))
    return robots

def calculate_positions(robots, steps, width, height):
    positions = []
    for x, y, dx, dy in robots:
        final_x = (x + dx * steps) % width
        final_y = (y + dy * steps) % height
        positions.append((final_x, final_y))
    return positions

def draw_pattern(positions, width, height):
    if not positions:
        return ""
    xs = [x for x, y in positions]
    ys = [y for x, y in positions]
    center_x = int(median(xs))
    center_y = int(median(ys))
    grid_size = 20 
    grid = [['.'] * grid_size for _ in range(grid_size)]
    for x, y in positions:
        nx = (x - center_x + grid_size//2) % grid_size
        ny = (y - center_y + grid_size//2) % grid_size
        if 0 <= nx < grid_size and 0 <= ny < grid_size:
            grid[ny][nx] = '#'
    return '\n'.join(''.join(row) for row in grid)

def solve(input_text):
    robots = parse_input(input_text)
    width, height = 101, 103
    positions_100 = calculate_positions(robots, 100, width, height)
    quadrants = defaultdict(int)
    for x, y in positions_100:
        if x == width // 2 or y == height // 2:
            continue
        quad = (1 if x < width//2 else 2) if y < height//2 else (3 if x < width//2 else 4)
        quadrants[quad] += 1
    safety_factor = 1
    for q in range(1, 5):
        safety_factor *= quadrants[q]
    for step in range(1, 301): 
        positions = calculate_positions(robots, step, width, height)
        pattern = draw_pattern(positions, width, height)
        print(f"\nStep {step}:")
        print(pattern)
        if step % 10 == 0:
            input("Press Enter to continue...")  
    
    return safety_factor

with open('/Users/.../Advent-Of-Code/2024/input.txt') as f:
    input_text = f.read()

print(solve(input_text))