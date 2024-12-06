from itertools import tee
import re

def part1(text):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.finditer(pattern, text)
    sum = 0; 
    multiplications = []
    for match in matches:
        x, y = map(int, match.groups())
        sum = sum + x * y 
    print(sum)

def part2(text):
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    mult_pattern = r'mul\((\d+),(\d+)\)'

    mults = [(m.start(), 'mul', m.groups()) for m in re.finditer(mult_pattern, text)]
    dos = [(m.start(), 'do', None) for m in re.finditer(do_pattern, text)]
    donts = [(m.start(), 'dont', None) for m in re.finditer(dont_pattern, text)]
    all_instructions = sorted(mults + dos + donts)
    #print(all_instructions)
    sum = 0
    enabled = True
    for pos, inst_type, groups in all_instructions:
        if inst_type == 'do':
            enabled = True
        elif inst_type == 'dont':
            enabled = False
        elif inst_type == 'mul' and enabled:
            x, y = map(int, groups)
            sum += x * y
    
    print(sum)

with open('/Users/.../Advent-Of-Code/2024/input.txt') as f:
    inputLines = f.read()
    part1(inputLines)
    part2(inputLines)

