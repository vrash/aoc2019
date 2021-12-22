import sys
from collections import defaultdict
import itertools as it
from copy import deepcopy

with open('/Users/vrashabhirde/Desktop/Advent-Of-Code/2021/input.txt') as f:
    input = list(f.read().splitlines())

D1 = defaultdict(int)
D2 = defaultdict(int)
for line in input:
    start,end = line.split('->')
    x1,y1 = start.split(',')
    x2,y2 = end.split(',')
    x1 = int(x1.strip())
    y1 = int(y1.strip())
    x2 = int(x2.strip())
    y2 = int(y2.strip())
    dx = x2-x1
    dy = y2-y1

    for i in range (1+max(abs(dx),abs(dy))):
        x = x1+(1 if dx>0 else(-1 if dx<0 else 0)) * i
        y = y1+(1 if dy>0 else(-1 if dy<0 else 0)) * i
        if dx==0 or dy==0:
            D1[(x,y)] += 1
        D2[(x,y)] +=1
    
#part 1
print(len([k for k in D1 if D1[k]>1]))
#part 2
print(len([k for k in D2 if D2[k]>1]))
