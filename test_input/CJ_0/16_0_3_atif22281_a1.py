import itertools as it
import math
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]
t=input()
s=input().split()
n=16
j=50
c=0
l=list(it.product('01',repeat=14))
print("Case #1:")
#p=[]
for i in l:
    f=0
    s='1'+"".join(i)+'1'
    for k in range(2,11):
        if(is_prime(int(s,k))):
            f=1
            break
    if f==0:
        c+=1
        o=str(s)
        for k in range(2,11):
            num=int(s,k)
            if num%2==0:
                o=o+" "+str(2)
            else:
                for q in range(3,int(math.sqrt(num)),2):
                    if num%q==0:
                        o=o+" "+str(q)
                        break
        print(o)
        #p.append(s)
    if c==50:
        break
