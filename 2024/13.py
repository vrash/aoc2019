#H/T Jonathan Paulson - direct SAT solver using z3 vs my original monstrous solution

import sys
from z3 import *
import re
def ints(s): #nice
    return [int(x) for x in re.findall('\d+', s)]
file = open('/Users/..../Desktop/Advent-Of-Code/2024/input.txt').read().strip()
def solve(ax,ay,bx,by,px,py,part2):
    P2 = 10000000000000 if part2 else 0
    px += P2
    py += P2
    t1 = z3.Int('t1')
    t2 = z3.Int('t2')
    SOLVE = z3.Solver()
    SOLVE.add(t1>0)
    SOLVE.add(t2>0)
    SOLVE.add(t1*ax+t2*bx == px)
    SOLVE.add(t1*ay+t2*by == py)
    if SOLVE.check() == z3.sat:
        M = SOLVE.model()
        ret = M.eval(3*t1+t2).as_long()
        return ret
    else:
        return 0
machines = file.split('\n\n')
part1 = 0 
part2 = 0
for i,machine in enumerate(machines):
    ax,ay,bx,by,px,py = ints(machine)
    part1 += solve(ax,ay,bx,by,px,py, False)
    part2 += solve(ax,ay,bx,by,px,py, True)
print('part1:', part1)
print('part2:', part2)