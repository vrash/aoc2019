from collections import deque
from heapq import heappush, heappop

def parse_input(input_text):
    coords = []
    for line in input_text.strip().split('\n'):
        x, y = map(int, line.split(','))
        coords.append((x, y))
    return coords

def drmanhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def astarlight(fallguy, grid_size, max_time):
    start = (0, 0)
    target = (grid_size - 1, grid_size - 1)
    corrupt = set(pos for i, pos in enumerate(fallguy) if i < max_time)
    
    if start in corrupt or target in corrupt:
        return None
        
    queue = [(drmanhattan(start, target), 0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: drmanhattan(start, target)}
    
    while queue:
        _, current_g, current = heappop(queue)
        
        if current == target:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return len(path) - 1
            
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_pos = (current[0] + dx, current[1] + dy)
            
            if not (0 <= next_pos[0] < grid_size and 0 <= next_pos[1] < grid_size):
                continue
                
            if next_pos in corrupt:
                continue
                
            tentative_g = current_g + 1
            
            if next_pos not in g_score or tentative_g < g_score[next_pos]:
                came_from[next_pos] = current
                g_score[next_pos] = tentative_g
                f = tentative_g + drmanhattan(next_pos, target)
                f_score[next_pos] = f
                heappush(queue, (f, tentative_g, next_pos))
    return None

def part1(input_text, grid_size=71, max_bytes=1024):
    fallguy = parse_input(input_text)
    return astarlight(fallguy, grid_size, max_bytes)

def part2(input_text, grid_size=71):
    fallguy = parse_input(input_text)
    left = 1
    right = len(fallguy)
    
    while left < right:
        mid = (left + right) // 2
        if astarlight(fallguy, grid_size, mid) is None:
            right = mid
        else:
            left = mid + 1
            
    blocking_byte = fallguy[left - 1]
    return f"{blocking_byte[0]},{blocking_byte[1]}"

with open('/Users/../Advent-Of-Code/2024/input.txt') as f:
    input_text = f.read()
print(part1(input_text))
print(part2(input_text))