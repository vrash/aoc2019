from collections import defaultdict, deque
def solve(input_text: str, max_jump=2, min_saving=100) -> int:
    track = set()
    start = end = 0j
    for y, row in enumerate(input_text.splitlines()):
        for x, c in enumerate(row):
            pos = complex(x, y)
            if c == 'S':
                start = pos
            elif c == 'E':
                end = pos
            if c != '#':
                track.add(pos)
    def get_distances(from_pos):
        dist = {from_pos: 0}
        queue = deque([(from_pos, 0)])
        while queue:
            pos, d = queue.popleft()
            d1 = d + 1
            for move in (1, -1, 1j, -1j):
                next_pos = pos + move
                if next_pos in track and next_pos not in dist:
                    dist[next_pos] = d1
                    queue.append((next_pos, d1))
        return dist
    forward = get_distances(start)
    backward = get_distances(end)
    fair_route = forward[end]
    savings = defaultdict(int)
    jumps = set()
    for y in range(-max_jump, max_jump + 1):
        for x in range(-max_jump, max_jump + 1):
            dist = abs(x) + abs(y)
            if 2 <= dist <= max_jump:
                jumps.add(complex(x, y))
    for pos in forward:
        for jump in jumps:
            jump_end = pos + jump
            if jump_end in backward:
                cheat = forward[pos] + abs(jump.real) + abs(jump.imag) + backward[jump_end]
                if cheat < fair_route:
                    savings[fair_route - cheat] += 1
    return sum(count for saving, count in savings.items() if saving >= min_saving)

with open('/Users/.../Advent-Of-Code/2024/input.txt') as f:
    input_text = f.read()
    print(solve(input_text))
    print(solve(input_text, 20))