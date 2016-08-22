import sys
import itertools


def is_jamcoin(x):
    return all((int(x, b) % (b + 1) == 0 for b in range(2, 11)))

def prove_jamcoin(x, f):
    print(x, "3 4 5 6 7 8 9 10 11", file=f)

def subsets(it):
   for i in range(len(it)+1):
       for s in itertools.combinations(it, i):
           yield s

def generate_jamcoins(n):
    template = '1'+(n-2)*'0'+'1'
    for ones_positions in subsets(range(1, n-1, 2)):
        t = list(template)
        for p in ones_positions:
            t[p] = '1'
            t[p+1] = '1'
        yield ''.join(t)

(n, j) = tuple(map(int, next(sys.stdin).strip().split(' ')))

with open('out'+str(n)+'.txt', 'w') as f:
    print('Case #1:', file=f)
    for jc in itertools.islice(generate_jamcoins(n), j):
        if is_jamcoin(jc):
            prove_jamcoin(jc, f)
