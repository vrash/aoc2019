from functools import cache
from random import random

codes =[]
def solve(codes, depths=[3, 26], its=1000):
    N = {
    '7': 0,      # Top-left corner
    '8': 1,      # Top-center
    '9': 2,      # Top-right
    '4': 1j,     # Middle-left
    '5': 1+1j,   # Center
    '6': 2+1j,   # Middle-right
    '1': 2j,     # Bottom-left
    '2': 1+2j,   # Bottom-center
    '3': 2+2j,   # Bottom-right
    ' ': 3j,     # Empty space
    '0': 1+3j,   # Bottom-near corner
    'A': 2+3j    # Bottom-far corner
}
    R = {
    ' ': 0,      # Initial position
    '^': 1,      # Up
    'A': 2,      # Activate
    '<': 1j,     # Left
    'v': 1+1j,   # Down
    '>': 2+1j    # Right
}

    @cache
    def path(start, end):
        pad = N if (start in N and end in N) else R
        diff = pad[end] - pad[start]
        dx, dy = int(diff.real), int(diff.imag)
        yy = ("^"*-dy) + ("v"*dy)
        xx = ("<"*-dx) + (">"*dx)

        if pad[start] + dy*1j == pad[" "]:
            return xx + yy + "A"
        if pad[start] + dx == pad[" "]:
            return yy + xx + "A"
        return (xx+yy if random() < 0.5 else yy+xx) + "A"
    
    @cache
    def length(code, depth, s=0):
        if depth == 0: return len(code)
        for i, c in enumerate(code):
            s += length(path(code[i-1], c), depth-1)
        return s
    def single_solve(code, max_depth):
        path.cache_clear()
        length.cache_clear()
        return int(code[:-1]) * length(code, max_depth)
    def single_simulate(code, max_depth):
        return min(single_solve(code, max_depth) for _ in range(its))
    return [sum(single_simulate(code, depth) for code in codes) for depth in depths]

with open('/Users/Vrash.Irde/Desktop/Advent-Of-Code/2024/input.txt', 'r') as f:
        codes = f.read().split()
results = solve(codes)
print(results[0])
print(results[1])