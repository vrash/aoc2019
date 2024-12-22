from collections import defaultdict
from pathlib import Path

def solve(text: str):
    codes = [int(line.strip()) for line in text.splitlines() if line.strip()]
    part1 = 0
    totals = defaultdict(int)
    
    for code in codes:
        secret = code
        sequence = (None, None, None, None)
        seen = set()
        for i in range(2000):
            if i == 1999:
                part1 += secret
            last_price = secret % 10
            secret = (secret ^ (secret << 6)) & 0xffffff
            secret = secret ^ (secret >> 5)
            secret = (secret ^ (secret << 11)) & 0xffffff
            sequence = (*sequence[1:], secret % 10 - last_price)
            if i >= 3 and sequence not in seen:
                seen.add(sequence)
                totals[sequence] += secret % 10
    return part1, max(totals.values())

p1, p2 = solve(Path("/Users/.../Advent-Of-Code/2024/input.txt").read_text())
print(p1)
print(p2)