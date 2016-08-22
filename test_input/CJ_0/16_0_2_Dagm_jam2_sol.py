import sys

inFileName = sys.argv[1]
outFileName = sys.argv[2]

inFile = open(inFileName,'r')
outFile = open(outFileName,'w')

def leastMoves(layout):
    if len(layout)==1:
        return int(layout=='-')
    moves = 0
    sign = layout[0]
    newSign = '-'*int(sign!='-') + '+'*int(sign!='+') 
    for i in range(1,len(layout)):
        if layout[i] != sign:
            layout = newSign*i + layout[i:]
            sign = layout[i]
            newSign = '-'*int(sign!='-') + '+'*int(sign!='+')
            moves += 1

    moves += layout[0]=='-'
    return moves
        

caseNums = int(inFile.readline().strip("\n"))
case = 0
for line in inFile:
    case += 1
    stack = line.strip('\n')

    outFile.write("Case #{}: {}\n".format(case, leastMoves(stack)))
    
inFile.close()
outFile.close()
            
