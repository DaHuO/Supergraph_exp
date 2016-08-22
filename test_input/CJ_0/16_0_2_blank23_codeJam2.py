def findPancakeFlips(curr, n):
    if len(n) == 0:
        if curr == "-":
            return 1
        else:
            return 0
    else:
        if curr != n[0]:
            return 1 + findPancakeFlips(n[0], n[1:])
        else:
            return findPancakeFlips(n[0], n[1:])

f = open('B-large.in', 'r')
g = open('output.txt', 'w')
inputs = []
for line in f:
    inputs.append(line)

testCases = int(inputs[0])
for caseNum in xrange(testCases):
    n = inputs[caseNum+1].strip()
    flips = findPancakeFlips(n[0], n[1:])

    g.write("Case #" + str(caseNum+1) + ": " + str(flips) + "\n")
    
f.close()
g.close()