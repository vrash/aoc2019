def solve(input_text):
    parts = input_text.strip().split('\n\n')
    patterns = [p.strip() for p in parts[0].split(',')]
    designs = [d.strip() for d in parts[1].splitlines()]
    cache = {}
    ways_cache = {}
    def can_make(design):
        if not design:
            return True
        if design in cache:
            return cache[design]
        
        for pattern in patterns:
            if design.startswith(pattern) and can_make(design[len(pattern):]):
                cache[design] = True
                return True          
        cache[design] = False
        return False
        
    def count_ways(design):
        if not design:
            return 1
        if design in ways_cache:
            return ways_cache[design] 
        total = 0
        for pattern in patterns:
            if design.startswith(pattern):
                total += count_ways(design[len(pattern):])
        ways_cache[design] = total
        return total
    part1 = sum(1 for design in designs if can_make(design))
    part2 = sum(count_ways(design) if can_make(design) else 0 for design in designs)
    return part1, part2

with open('/Users/..../Advent-Of-Code/2024/input.txt') as f:
    p1, p2 = solve(f.read())
    print(p1, p2)