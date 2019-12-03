lo = open("/Users/vrashabhirde/Desktop/aoc/input.txt").read().split(",")
#part 2
for a in range(100):
    for b in range(100):
        l = [int(i) for i in lo]
        OP = 0
        X = 1
        Y = 2
        Z = 3
        l[X] = a
        l[Y] = b
        while True:
            op = l[OP]
            if(op==99):
                break
            x = l[l[X]]
            y = l[l[Y]]
            if(op == 1):
                l[l[Z]] = x + y
            elif(op == 2):
                l[l[Z]] = x * y
            OP = OP + 4
            X = X + 4
            Y = Y + 4
            Z = Z + 4
        if(l[0] == 19690720):
            print(100 * a + b)
