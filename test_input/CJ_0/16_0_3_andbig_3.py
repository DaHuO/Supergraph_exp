import math

def getpows(n):
    return [[i**j for j in range(n)] for i in range(2,11)]
    
def getinitsums(pows):
    return [pl[0] + pl[-1] for pl in pows]
    
# returns none if prime
def getdivisor(n):
    if n <= 2:
        return None
    i=2
    sq=int(math.sqrt(n))
    while i <= sq:
        if n % i == 0:
            return i
        i+=1
    return None

# returns none if at lest 1 is prime    
def getdivisors(sums):
    divisors=[]
    for s in sums:
        d = getdivisor(s)
        if d is None:
            return None
        divisors.append(d)
    return divisors
    
def rec(pows,sums,j,sols,maxdepth,depth):
    if len(sols) >= j:
        return

    if depth > maxdepth:
        # check if all sums are prime
        divisors = getdivisors(sums)
        if not divisors is None:
            sols.append((str(sums[-1]),divisors))
        return
        
    rec(pows,sums,j,sols,maxdepth,depth+1)
    
    for i in range(9):
        sums[i] += pows[i][depth]
    
    rec(pows,sums,j,sols,maxdepth,depth+1)
        
    for i in range(9):
        sums[i] -= pows[i][depth]
        
    return
        
    
def getans(n,j):
    pows = getpows(n)
    sums = getinitsums(pows)
    maxdepth = n-2
    depth=1
    sols=[]
    
    rec(pows,sums,j,sols,maxdepth,depth)
    if len(sols) != j:
        print "FAIL"
    return sols
    
fileName = "small_crafted.in"
f = open(fileName)

l=f.readline()
l=f.readline()

inputs=[]
while l:
    inputs.append(l[:-1])
    l=f.readline()
    
f.close()

#print inputs

outfile=fileName+".out"
of=open(outfile,"wb")
testCount=1

for inputEl in inputs:
    n,j = [int(x) for x in inputEl.split(' ')]
    #print str(n) + " " + str(j)
    ans = getans(n,j)
    of.write("Case #" + str(testCount) + ":\n")
    
    for a in ans:
        of.write(str(a[0]) + " " + ' '.join([str(x) for x in a[1]]) + "\n")
    testCount += 1

of.close()
