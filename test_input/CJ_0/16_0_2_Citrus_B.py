fOut = open('B-large.out', 'w')
with open('B-large.in', 'r') as f:
    testCases = int(f.readline().strip('\n'))
    
    for i in range(testCases):
        s = f.readline().strip('\n')
        turns = 0
        index = 0
        while index != -1:
            side = s[index]
            opSide = '+' if side == '-' else '-'
            index = s.find(opSide, index)
            if index != -1:
                turns += 1
        if s.endswith('-'):
            turns += 1
        fOut.write("Case #" + str(i+1) + ": " + str(turns) + '\n')

fOut.close()
