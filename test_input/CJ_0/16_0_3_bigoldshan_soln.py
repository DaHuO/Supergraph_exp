import sys
import random

inp = sys.stdin
inp = open("C-large.in","r")
outp = open("out","w")
#outp = sys.stdout
def read_inp():
    return inp.readline().strip()


def interpret(coin, b):
    s = 0
    for i,d in enumerate(coin):
        s += d*b**(len(coin)-i-1)
    return s

def sqrt(v):
    x = v
    diff = 2
    while diff > 1:
        x1 = (x+v/x)/2
        diff = abs(x1 - x)
        x = x1
    return x

def divisor(v):
#    print v, sqrt(v)
    sv = min(sqrt(v),1000)
    for i in xrange(2,sv):
#        d = random.randint(2, sv)
        if v %i == 0:
            return i
    return None
    
    
T = int(read_inp())

for t in xrange(1,T+1):
    N,J = [int(s) for s in read_inp().split()]
    
    ans = []
    coins = set()
    for i in xrange(J):
        while True:
            coin = [1] + [random.randint(0,1) for _ in xrange(N-2)] + [1]
            coinstr = ''.join([str(c) for c in coin])
            if coinstr in coins:
                continue
            divisors = []
            for j in xrange(2, 11):
                v = interpret(coin, j)
                d = divisor(v)
                #print ''.join([str(c) for c in coin]),j,v,d
                if d is None:
#                    print i,j,v,coinstr
                    break
                divisors.append(str(d))
            else:
                coins.add(coinstr)
                break
#        print coin,divisors
        ans.append(' '.join([''.join([str(c) for c in coin])] + divisors))
    
    outp.write("Case #%d:\n%s"%(t,'\n'.join(ans)))

outp.close()