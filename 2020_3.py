import fileinput

Forest = []
givenSlopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

for line in fileinput.input():
    Forest.append(list(line.strip()))

treeCount1 = 1
treeCount2 = 1

for(treeCol,treeRow) in givenSlopes:
    rowCount = 0
    colCount = 0
    slopeCount = 0
    while rowCount+1 <len(Forest):
        colCount += treeCol
        rowCount += treeRow
        if Forest[rowCount][colCount%len(Forest[rowCount])]=='#':
            slopeCount += 1
    if(treeCol == 3 and treeRow==1):
        treeCount1 = slopeCount
    treeCount2 *= slopeCount
print(treeCount1)
print(treeCount2)
            
    

                
