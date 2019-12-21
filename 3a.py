import math

X,Y = open("/Users/slartibartfast/Downloads/aoc2019/3.txt").read().split('\n')
X,Y = [x.split(',') for x in [X,Y]]


DictX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DictY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}


def traceAllPoints(inputt):
    ans = {}
    x = 0
    y = 0
    length = 0
   
    for inp in inputt:
        d = inp[0]
        n = int(inp[1:])
        for i in range(n):
            x += DictX[d]
            y += DictY[d]
            length += 1
            #print length
             
            if (x,y) not in ans:
                ans[(x,y)] = length
                #print ans
    return ans


pointsInX = traceAllPoints(X)
pointsInY = traceAllPoints(Y)
intersectXY = set(pointsInX.keys())&set(pointsInY.keys())

#part1
#ans1 = min([x+y for (x,y) in intersectXY])
ans1 = min([abs(x)+abs(y) for (x,y) in intersectXY])
print(ans1)

#part2
ans2 = min([pointsInX[point] + pointsInY[point] for point in intersectXY])
print(ans2)
