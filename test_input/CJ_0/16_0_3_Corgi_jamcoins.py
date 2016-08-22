def getnext( binrep ):
    signif = binrep[1:len(binrep) - 1]
    curr = len(signif) - 1
    
    while signif[curr] == 1 and curr >= 0:
        signif[curr] = 0
        curr -= 1
    if curr >= 0:
        signif[curr] = 1
    else:
        return False
    return [1] + signif + [1]    

def getnum( base, binrep ):
    l = len(binrep)
    res = 0
    for i in range(0, l):
        res += binrep[l - i - 1]*base**i
    return res

def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

def isJam (binrep, base):
    return not IsPrime(getnum(base, binrep))

def checkprime( num ):
    divisor = 1
    i = 1
    while divisor == 1 and  i * i < num:
        i += 1
        if num % i == 0:
            return i
    return 0

def put(binrep, base, s):
    if not IsPrime(getnum(base, binrep)):
        s.add(tuple(binrep))

def getdiv( binrep ):
    res = []
    for x in range(2, 11):
        res.append(str(checkprime(getnum(x, binrep))))
    return res

fin = open('coins.in', 'r')
fout = open('coins.out', 'w')

t = int(fin.readline())
n,j = map(int, fin.readline().split())

mins = [1] + [0] * (n - 2) + [1]

s = set()
count = 0;
binrep = mins
while binrep and count < j:
    if  isJam(binrep, 2) and isJam(binrep, 3) and isJam(binrep, 4) and isJam(binrep, 5) and isJam(binrep, 6) and isJam(binrep, 7) and isJam(binrep, 8) and isJam(binrep, 9) and isJam(binrep, 10):
        s.add(tuple(binrep))
        count += 1
    binrep = getnext(binrep)

U = s

fout.write("Case #1: \n")
i = 0

for b in U:
    print ("Prime!")
    if i < j:
        s = ''
        for c in b:
            s += str(c)
        divisors = getdiv(b)
        s +=  ' ' + ' '.join(divisors)
        fout.write(s + '\n')
        i += 1