import random
from sympy import divisors
from itertools import islice

def get_random_bitstring(n):
    ds = (n - 2)
    fs = '{0:0%ib}' % ds
    return '1' + fs.format(random.randint(0,2**ds - 1)) + '1'

def to_base(s, b):
    return int(s, b)

def get_divisor(n):
    ds = list(islice(divisors(n, generator=True), 1, 2))
    if not ds:
        return 1
    if ds[0] == n:
        return 1
    return ds[0]

input()
N,J = [int(x) for x in input().split()]

strings = {}
while len(strings) < J:
    s = get_random_bitstring(N)
    if s in strings:
        continue
    ok = True
    fs = []
    for b in range(2, 10 + 1):
        f = get_divisor(to_base(s, b))
        if(f <= 1):
            ok = False
            break
        fs.append(f)            
    
    if not ok:
        continue

    strings[s] = fs

print('Case #1:')
for k, v in strings.items():
    print(k, ' '.join(map(str, v)))