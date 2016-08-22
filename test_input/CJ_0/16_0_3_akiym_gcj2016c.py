# -*- coding: utf-8 -*-

T = input()
N = input()
J = input()
#N = 6
#J = 3
#N = 16
#J = 50
#N = 32
#J = 500

def is_prime(q,k=100):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    for i in xrange(3,k):
        x,y = q,i
        while y:
            x, y =  y, x % y
        if x != 1: continue
        if pow(i, q-1, q) != 1:
            return False
    return True

print 'Case #1:'

cnt = 0
for i in xrange(2**(N-2)):
    ok = True
    ns = []
    for j in xrange(2, 11):
        n = (j**(N-1)) + 1
        m = i
        for k in range(N-2):
            if m & 1:
                n += j ** (k + 1)
            m >>= 1
        if is_prime(n):
            ok = False
            break
        ns.append(n)
    if ok:
        print bin((2**(N-1)) + (i*2) + 1)[2:],
        divs = []
        for n in ns:
            for k in xrange(2, n):
                if n % k == 0:
                    divs.append(str(k))
                    break
        print ' '.join(divs)

        cnt += 1
        if cnt == J:
            break
