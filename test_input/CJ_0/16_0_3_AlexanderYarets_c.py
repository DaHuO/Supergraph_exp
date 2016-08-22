import sys

def getd(n):
    for i in range(2, 50):
        if n % i == 0:
            return i
    return None

t = int(raw_input().strip())
for a0 in xrange(t):
    print 'Case #' + str(a0 + 1) + ':'
    n, j = map(int, raw_input().strip().split())
    for i in xrange(2**(n-2)):
        t = bin(i)[2:]
        coin = '1' + '0'*(n-2-len(t)) + t + '1'

        d = []
        for p in range(2, 11):
            x = int(coin, p)
            dd = getd(x)
            if dd == None:
                break
            d.append(dd)
        
        if len(d) == 9:
            print coin + ' ' + ' '.join(map(str, d))
            j -= 1
        if j == 0:
            break
