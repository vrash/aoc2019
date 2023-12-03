import sys
import re
from collections import defaultdict

with open('/Users/.../Desktop/Advent-of-Code/2023/input.txt') as f:
    inputLines = f.read()

lines = inputLines.split('\n')
R = len(lines)
C = len(lines[0])


#return symbol
def find_symbol(x,y):
  if 0<=x<C and 0<=y<R and lines[y][x]!="." and not lines[y][x].isdigit():
    return (lines[y][x],(x,y))
  return None

    
part1 = 0
part2 = 0

gears=defaultdict(list)

for y,line in enumerate(lines):
  i=0
  #print(line)
  while i<len(line):
     #keep track of start and end position of a number
    if line[i].isdigit():
      leftMost=i-1
      rightMost = i

      #iterate through line, until not a digit to grab a full number
      while rightMost<len(line) and line[rightMost].isdigit():
        rightMost = rightMost + 1
      #build the number
      n = int(line[leftMost+1:rightMost])

      #check if there's an adjacent symbol to number
      nearestSymbol = find_symbol(leftMost,y) or find_symbol(rightMost,y)

      #diagonal check
      for pos in range(leftMost,rightMost+1):
        nearestSymbol = (nearestSymbol or find_symbol(pos,y-1) or find_symbol(pos,y+1))

      if nearestSymbol:
        
        part1+=n
        #part2
        symbol,pos = nearestSymbol
        #if star then append numbers together in the dict
        if symbol == "*":
          gears[pos].append(n)

      i=rightMost

    else:
      i=i+1

for gear in gears.values():
  #check dict if there are exactly two values
  if len(gear)==2:
    part2 = part2 + gear[0] * gear[1]

print(part1)
print(part2)




        
  
  
