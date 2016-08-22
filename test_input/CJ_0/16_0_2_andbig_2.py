def countchanges(s):
    count=0
    if len(s) == 0:
        return 0
    cur=s[0]
    for c in s:
        if cur != c:
            cur = c
            count += 1
    return count

def getans(e):
    if len(e) == 0:
        return 0
    return countchanges(e+"+")

fileName = "B-large.in"
f = open(fileName)

l=f.readline()
l=f.readline()

inputs=[]
while l:
    inputs.append(l[:-1])
    l=f.readline()
    
f.close()

#print inputs

outfile="tst2.out"
of=open(outfile,"wb")
testCount=1

for inputEl in inputs:
    ans = getans(inputEl)
    of.write("Case #" + str(testCount) + ": " + str(ans)+'\n')
    testCount += 1

of.close()
