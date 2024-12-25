def solve(text):
    locks, keys = [], []
    for section in text.strip().split('\n\n'):
        lines = section.splitlines()
        heights = []
        if '#' in lines[0]:
            for col in range(len(lines[0])):
                count = sum(1 for row in range(len(lines)) if lines[row][col] == '#')
                heights.append(count)
            locks.append(heights)
        else:
            for col in range(len(lines[0])):
                count = sum(1 for row in range(len(lines)-1, -1, -1) if lines[row][col] == '#')
                heights.append(count)
            keys.append(heights)
    
    rows = len(text.strip().split('\n\n')[0].splitlines())
    return sum(1 for lock in locks for key in keys 
              if all(l + k <= rows for l, k in zip(lock, key)))

print(solve(Path("/Users/Vrash.Irde/Desktop/Advent-Of-Code/2024/input.txt").read_text()))