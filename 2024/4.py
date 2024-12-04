from itertools import tee
import re

def part1(matrix):
    part1_ans = 0
    word = "XMAS"
    dir = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for dx, dy in dir:
                if all(0 <= i + k * dx < len(matrix) and 0 <= j + k * dy < len(matrix[i]) and matrix[i + k * dx][j + k * dy] == word[k] for k in range(len(word))):
                    part1_ans += 1
    return part1_ans

def part2(matrix):
    part2_ans = 0
    for i in range(len(matrix) - 2):  
        for j in range(1, len(matrix[i]) - 1):  
            diag1 = [matrix[i+k][j-1+k] for k in range(3)] 
            diag2 = [matrix[i+k][j+1-k] for k in range(3)] 
            diag1_str = ''.join(diag1)
            diag2_str = ''.join(diag2)
            if ((diag1_str == "SAM" or diag1_str == "MAS") and 
                (diag2_str =="SAM" or diag2_str == "MAS")):
                part2_ans += 1
                
    return part2_ans

with open('/Users/.../Advent-Of-Code/2024/input.txt') as f:
    inputLines = f.read()
    matrix = [list(line) for line in inputLines.splitlines()]

print(part1(matrix))
print(part2(matrix))
