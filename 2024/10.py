

rows =0 
cols=0

def part1(height_map):
    total_score = 0
    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols
    def dfs(x, y, visited):
        if not in_bounds(x, y) or (x, y) in visited or height_map[x][y] == -1:
            return 0
        visited.add((x, y))
        score = 1 if height_map[x][y] == 9 else 0
        current_height = height_map[x][y]
        height_map[x][y] = -1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and height_map[nx][ny] == current_height + 1:
                score += dfs(nx, ny, visited)
        height_map[x][y] = current_height
        return score
    for i in range(rows):
        for j in range(cols):
            if height_map[i][j] == 0: 
                visited = set()
                total_score += dfs(i, j, visited)
    
    return total_score

def part2(height_map):
    total_rating = 0
    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols
    def count_trails(start_x, start_y):
        def dfs(x, y, path):
            if not in_bounds(x, y):
                return 0
            current_height = height_map[x][y]
            if len(path) > 0 and current_height != path[-1][2] + 1:
                return 0
            if current_height == 9:
                return 1
            total = 0
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if (nx, ny) not in {(x, y) for x, y, _ in path}:
                    path.append((x, y, current_height))
                    total += dfs(nx, ny, path)
                    path.pop()
            return total
        trails = 0
        for nx, ny in [(start_x+1, start_y), (start_x-1, start_y), 
                       (start_x, start_y+1), (start_x, start_y-1)]:
            if in_bounds(nx, ny) and height_map[nx][ny] == 1:
                trails += dfs(nx, ny, [])
        
        return trails
    
    for i in range(rows):
        for j in range(cols):
            if height_map[i][j] == 0:
                rating = count_trails(i, j)
                total_rating += rating
    
    return total_rating

with open('/Users/.../Desktop/Advent-Of-Code/2024/input.txt') as f:
    input_text = f.read()
    height_map = [list(map(int, line)) for line in input_text.splitlines()]
    rows = len(height_map)
    cols = len(height_map[0])
    print(part1(height_map))
    print(part2(height_map))