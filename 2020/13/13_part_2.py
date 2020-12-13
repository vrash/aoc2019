import functools
from functools import reduce

with open("/Users/vrashabhirde/Desktop/Desk/aoc1/input.txt") as f:
    input = f.read().strip().split("\n")
bus = input[1].split(",")

#python instead of java to prevent using biginteger nonsense
#https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

n = []
a = []

for i,x in enumerate(bus):
    if x == "x":
        continue
    n.append(int(x))
    a.append(-i)

#print(n, a)
print(chinese_remainder(n, a))
