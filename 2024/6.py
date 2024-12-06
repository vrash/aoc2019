directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
def part1(grid, start_pos, start_dir):
    current_pos = start_pos
    current_dir = start_dir
    visited = {current_pos}
    
    rows, cols = len(grid), len(grid[0])
    
    while True:
        dr, dc = directions[current_dir]
        next_row = current_pos[0] + dr
        next_col = current_pos[1] + dc
        if (next_row < 0 or next_row >= rows or 
            next_col < 0 or next_col >= cols or 
            grid[next_row][next_col] == '#'):
            current_dir = turn_right[current_dir]
            continue
        current_pos = (next_row, next_col)
        visited.add(current_pos)
        if (current_pos[0] == 0 or current_pos[0] == rows-1 or 
            current_pos[1] == 0 or current_pos[1] == cols-1):
            break
    return len(visited)

def parse_input(input_text):
    grid = []
    guard_pos = None
    guard_dir = None
    
    for row, line in enumerate(input_text.strip().splitlines()):
        grid_row = []
        for col, char in enumerate(line):
            if char in '^>v<':
                guard_pos = (row, col)
                guard_dir = char
                grid_row.append('.')
            else:
                grid_row.append(char)
        grid.append(grid_row)
    
    return grid, guard_pos, guard_dir

def is_loop_path(grid, start_pos, start_dir, test_pos):
    if test_pos == start_pos:  
        return False
    test_grid = [row[:] for row in grid]
    test_grid[test_pos[0]][test_pos[1]] = '#'
    curr = start_pos
    current_dir = start_dir
    visited_states = set() 
    rows, cols = len(grid), len(grid[0])
    max_steps = rows * cols * 4  #To prevent buzz light year from going to infinity and beyond
    steps = 0
    while steps < max_steps:
        steps += 1
        state = (curr, current_dir)
        
        if state in visited_states:
            return True
        visited_states.add(state)
        
        dr, dc = directions[current_dir]
        next_row = curr[0] + dr
        next_col = curr[1] + dc
        if (next_row < 0 or next_row >= rows or 
            next_col < 0 or next_col >= cols or 
            test_grid[next_row][next_col] == '#'):
            current_dir = turn_right[current_dir]
            continue
        curr = (next_row, next_col)
        if (curr[0] == 0 or curr[0] == rows-1 or 
            curr[1] == 0 or curr[1] == cols-1):
            return False
    return False

def part2(grid, start_pos, start_dir):
    loop_positions = set()
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if col < len(grid[row]) and grid[row][col] == '.' and (row, col) != start_pos:
                if is_loop_path(grid, start_pos, start_dir, (row, col)):
                    loop_positions.add((row, col))
    return len(loop_positions)

with open('/Users/.../Advent-Of-Code/2024/input.txt') as f:
    input_text = f.read()

grid, guard_pos, guard_dir = parse_input(input_text)
part1ans = part1(grid, guard_pos, guard_dir)
print(part1ans)
part2ans = part2(grid, guard_pos, guard_dir)
print(part2ans)
