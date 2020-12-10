import math

l = open("/Users/slartibartfast/Downloads/aoc2019/1.txt").read().splitlines()
sum = 0

#part 1
for i in l:
    sum += math.floor(int(i)/3)-2
print (sum)

#part 2 - improved for readability

sum = 0
for i in l:
    innersum = 0
    x = math.floor(int(i)/3)-2
    while(x>0):
        innersum += x
        x = math.floor(x/3)-2
    sum += innersum

print (sum)
