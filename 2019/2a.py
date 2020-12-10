lo = open("/Users/vrashabhirde/Desktop/aoc/input.txt").read().split(",")
l = [int(i) for i in lo]
OP = 0
X = 1
Y = 2
Z = 3
#part 1
for i in l:
    op = l[OP]
    if(op==99):
        print l[0]
        break
    x = l[l[X]]
    y = l[l[Y]]
    #print y
    if(op == 1):
        l[l[Z]] = x + y
    elif(op == 2):
        l[l[Z]] = x * y
        #print l[l[Z]]
    OP = OP + 4
    X = X + 4
    Y = Y + 4
    Z = Z + 4
    
