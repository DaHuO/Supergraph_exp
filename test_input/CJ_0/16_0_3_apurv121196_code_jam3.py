import itertools as it
from math import sqrt
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
n,j=input().split()
print("Case #1:")

l=list(it.product('01',repeat=int(n)-2))
#print(l)
nprime=[]
cnt=0
for f in l:
    k='1'+''.join(f)+'1'
    chk=0
    for i in range(2,11):
        if(is_prime(int(k,i))):
            chk=1
            break
    if chk==0:
        nprime.append(k)
        cnt+=1
    if cnt==int(j):
        break
for h in range(len(nprime)):
    divisors=[]
    for r in range(2,11):
        num=int(nprime[h],base=r)
        #print(num)
        if num%2==0:
            divisors.append(2)
        else:
            for u in range(3,int(sqrt(num)+1),2):
                if num%u==0:
                    divisors.append(u)
                    break
    print(nprime[h],divisors[0],divisors[1],divisors[2],divisors[3],divisors[4],divisors[5],divisors[6],divisors[7],divisors[8])
            
    
