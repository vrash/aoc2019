from collections import defaultdict, deque

with open('/Users/Vrash.Irde/Desktop/Advent-Of-Code/2024/input.txt') as f:
    input_text = f.read().strip()
grid = [list(line) for line in input_text.splitlines()]

def find(grid, part2=False):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    regions = []
    def count_sides(region, type):
        sides = set()
        horizontal_segments = set()
        vertical_segments = set()
        
        for r, c in region:
            for dr, dc in [(0,1), (1,0)]:
                nr, nc = r + dr, c + dc
                if (nr >= rows or nc >= cols or 
                    grid[nr][nc] != type):
                    if dr == 0: 
                        horizontal_segments.add((r, c))
                    else:  
                        vertical_segments.add((r, c))
        curr = []
        for r in range(rows):
            segments_in_row = sorted((r, c) for c in range(cols) 
                                   if (r, c) in horizontal_segments)
            
            for pos in segments_in_row:
                if not curr:
                    curr.append(pos)
                elif pos[1] != curr[-1][1] + 1:
                    sides.add(tuple(curr))
                    curr = [pos]
                else:
                    curr.append(pos)
            if curr:
                sides.add(tuple(curr))
                curr = []
        curr = []
        for c in range(cols):
            segments_in_col = sorted((r, c) for r in range(rows) 
                                   if (r, c) in vertical_segments)
            
            for pos in segments_in_col:
                if not curr:
                    curr.append(pos)
                elif pos[0] != curr[-1][0] + 1:
                    sides.add(tuple(curr))
                    curr = [pos]
                else:
                    curr.append(pos)
            if curr:
                sides.add(tuple(curr))
                curr = []
        
        return len(sides)
    
    def get_region(start, end):
        type = grid[start][end]
        region = set()
        perimeter = 0
        queue = deque([(start, end)])
        region.add((start, end))
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or 
                    grid[nr][nc] != type):
                    perimeter += 1
                    continue
                if (nr, nc) not in region:
                    region.add((nr, nc))
                    queue.append((nr, nc))
        region = list(region)
        sides_count = count_sides(region, type) if part2 else perimeter
        return region, perimeter, sides_count, type
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                region, perimeter, sides_count, type = get_region(r, c)
                regions.append((region, perimeter, sides_count, type))
                visited.update(region)
    
    return regions

def calc(regions, part2=False):
    total = 0
    for coords, perimeter, sides_count, type in regions:
        area = len(coords)
        price = area * (sides_count if part2 else perimeter)
        total += price
    return total

def solve(grid, part2=False):
    regions = find(grid, part2)
    total = calc(regions, part2)
    return total

part1 = solve(grid, False)
print(part1)
part2 = solve(grid, True)
print(part2)