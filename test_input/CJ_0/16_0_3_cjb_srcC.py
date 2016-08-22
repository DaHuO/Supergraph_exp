def base2str(i):
    if i == 0: return '0'
    if i == 1: return '1'
    return base2(i/2) + str(i%2)

def evalbasen(n, i):
    s = 0
    for x in i:
        s *= n
        s += int(x)
    return s

def gen(n):
    for i in range(0, 2**(n-2)):
        x = base2str(i)
        x = '0' * (n-2-len(x)) + x
        jc = '1{}1'.format(x)
        yield jc
def isprime(n):
    if n % 2 == 0:
        return False
    i = 3;
    while i * i <= n:
        i += 2;
        if n % i == 0:
            return False
    return True

def primes(n1, n2):
    if n1 <= 2:
        yield 2
    i = 3
    if n1 > i: 
        i = 2*(n1/2)+1
    while i < n2:
        if isprime(i):
            yield i
        i += 2

def sieve(coins, p1, p2):
    coins2 = set()
    for c in coins:
        iscoin = True
        for i in range(2, 11):
            q = evalbasen(i, c)
            #print c, i, q, isprime(q)
            if isprime(q):
                iscoin = False
        if iscoin:
            coins2.add(c)
    return coins2

def sieve2(coins, p1, p2):
    divisors = {}
    p = [x for x in primes(p1, p2)]
    #print p
    for c in coins:
        divisors[c] = []
        for b in range(2, 11):
            q = evalbasen(b, c)               
            for j in p:
                if q % j == 0 and j < q:
                    divisors[c] += [j]
                    break
    return divisors

s2 = sieve2([x for x in gen(16)], 1, 40)

q = [(k, v) for k, v in s2.iteritems() if len(v) >= 9]
print 'Case #1:'
ql = [(k,v) for k,v in s2.iteritems() if len(v) >= 9]
ql = ql[:50]

f = open('/Users/bosley/Desktop/C.out','w')
f.write('Case #1:\n')
for k, v in ql:
    print '{}'.format(k), ' '.join([str(x) for x in v])
    f.write('{} '.format(k) + ' '.join([str(x) for x in v]) + '\n')
f.close()
#print ql
