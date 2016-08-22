import math
def rec(s, n):
    if len(s[0]) < n:
        b = []
        for a in s:
            b.append(a+"0")
            b.append(a+"1")
        return rec(b,n)
    else:
        return s

def prime(n):
    for p in range(2,int(math.floor(math.sqrt(n)))+1):
        if n % p == 0:
            return p
    return 0

f = open('q3.txt', 'r')
i = 0

for s in f:
    if i == 0:
        i = i + 1
        case = s
        continue
    if i > int(case):
        break
    
    print "Case #%d:" % i
    n, j = s.split() 
    n = int(n)
    j = int(j)
    q = 0
    for x in rec(["0", "1"], n-2):
        word = "1"+x+"1"
        for n in range(2, 11):
            m = prime(int("1"+x+"1", n))
            if m == 0:
                break
            word = word + " " + str(m)
            if n == 10:
                print word
                q += 1
        if q >= j:
            break
    i = i + 1

f.close()
