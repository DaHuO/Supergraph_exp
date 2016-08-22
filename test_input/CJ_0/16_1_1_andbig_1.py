def getans(el):
    w=el[0]
    l=len(el)
    i = 1
    while i < l:
        c = el[i]
        if c != '\n':
            w = c + w if w[0] <= c else w + c
        i += 1
    return w

fileName = "A-large.in"
f = open(fileName)

l=f.readline()
l=f.readline()

inputs=[]
while l:
    inputs.append(l)
    l=f.readline()
    
f.close()

outfile="tst1.out"
of=open(outfile,"wb")
testCount=1

for inputEl in inputs:
    ans = getans(inputEl)
    of.write("Case #" + str(testCount) + ": " + str(ans)+'\n')
    testCount += 1

of.close()

