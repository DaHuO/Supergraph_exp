import sys
def sol(s):
    if len(s) == 1 or len(s) == 0:
        return s
    c = '0'
    cPos = -1
    i = 0
    for char in s:
        if char >= c:
            c = char
            cPos = i
        i += 1
    return c+sol(s[0:cPos])+s[cPos+1:]

sys.setrecursionlimit(1100)
fIn = open('input.txt', 'r')
fOut = open('output.txt', 'w')
case = 0
for line in fIn:
    print("Case: "+str(case))
    if case > 0:
        fOut.write("Case #"+str(case)+": "+sol(line))
    case += 1