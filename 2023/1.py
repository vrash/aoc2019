import sys
with open('/Users/.../Desktop/Advent-of-Code/2023/input.txt') as f:
    inputLines = f.read()
    
part1 = 0
part2 = 0

for line in inputLines.split('\n'):
  part1_digits = []
  part2_digits = []
  
  for i,c in enumerate(line):
    if c.isdigit():
      part1_digits.append(c)
      part2_digits.append(c)
      
    for d,val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
      if line[i:].startswith(val):
        part2_digits.append(str(d+1))

  part1 += int(part1_digits[0]+part1_digits[-1])
  part2 += int(part2_digits[0]+part2_digits[-1])

print(part1)
print(part2)
