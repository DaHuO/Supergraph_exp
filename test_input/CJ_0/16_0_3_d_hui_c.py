print "Case #1:"
p = []
def prime(x):
    global p
    for y in p:
        if x%y==0:
            return 0
    return 1
i = 2
n = 32
while i*i<=2**n:
    f=1
    for x in p:
        if i%x==0:
            f=0
            break
    if f:
        p=p+[i]
    i+=1
j = 500
c = 0
while c < 2**(n-2) and j>0:
    s = bin(c)[2:]
    while len(s) < n-2:
        s = '0' + s
    s = '1' + s + '1'
    f = 1
    for i in range(2, 11):
        if prime(int(s, i)):
            f=0
            break
    if f:
        o = [s]
        for i in range(2, 11):
            x = int(s, i)
            for y in p:
                if x % y == 0:
                    o+=[str(y)]
                    break
        print ' '.join(o)
        j -= 1
    c += 1
