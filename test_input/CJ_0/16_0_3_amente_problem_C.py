import fileinput

out_file = open('C-small', 'w');

N = 16
J = 50



from math import sqrt
from functools import lru_cache, reduce
from collections import Counter
from itertools import product

 
MUL = int.__mul__
 
 
def prime_factors(n):
    'Map prime factors to their multiplicity for n'
    d = _divs(n)
    d = [] if d == [n] else (d[:-1] if d[-1] == d else d)
    pf = Counter(d)
    return dict(pf)
 
@lru_cache(100000)
def _divs(n):
    'Memoized recursive function returning prime factors of n as a list'
    for i in range(2, int(sqrt(n)+1)):
        d, m  = divmod(n, i)
        if not m:
            return [i] + _divs(d)
    return [n]
 
 
def proper_divs(n):
    '''Return the set of proper divisors of n.'''
    pf = prime_factors(n)
    pfactors, occurrences = pf.keys(), pf.values()
    multiplicities = product(*(range(oc + 1) for oc in occurrences))
    divs = {reduce(MUL, (pf**m for pf, m in zip(pfactors, multis)), 1)
            for multis in multiplicities}
    try:
        divs.remove(n)
    except KeyError:
        pass
    return divs or ({1} if n != 1 else set())



import itertools

res = []
def solve():
    bases = range(2,11);
    for seq in itertools.product("01", repeat=N-2):
        c = "1"+"".join(seq)+"1"
        case_res = [c]
        for base in bases:
            d = proper_divs(int(c,base))
            #print d
            if(len(d) > 1):
                for e in d:
                    if not e == 1:
                        case_res.append(e)
                        break
        if len(case_res) == 10:
            res.append(case_res)
        
        if(len(res) == J):
            return
        
        

ans = "Case #1:"
out_file.write(ans + '\n')

solve()
for i in res:
    out_file.write(str(i).strip('[').strip(']').replace(',',' ') + '\n')

out_file.close()
