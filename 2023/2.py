import sys
from collections import defaultdict

with open('/Users/.../Desktop/Advent-of-Code/2023/input.txt') as f:
    inputLines = f.read()
    
part1 = 0
part2 = 0

for line in inputLines.split('\n'):
  id_, line = line.split(':')
  possible = True
  
  DICT = defaultdict(int)
  for event in line.split(';'):
    for balls in event.split(','):
      number,colour = balls.split()
      DICT[colour] = max(DICT[colour], int(number)) 
      if int(number)>{'red':12, 'green':13, 'blue':14}.get(colour,0):
        possible = False;
        
  #part1
  if(possible):
    part1= part1 + int(id_.split()[-1])

 #part2
  score = 1
  for ball in DICT.values():
    score  = score * ball
  part2 = part2 + score
    
print(part1)
print(part2)
