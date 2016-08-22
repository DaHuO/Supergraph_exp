from sys import argv
from collections import defaultdict
from math import sqrt
from itertools import product, count

seen = {}

def get_divisor(num):
    if (num % 2 == 0):
        seen[num] = 2
        return 2

    rt = int(sqrt(num))

    s = 0

    for i in xrange(seen.get(num, 3), rt, 2):
        if (num%i == 0):
            seen[num] = i
            return i
        s += 1
        if s > 5000:
            break

    seen[num] = None
    return None

def get_baserep(numarr, b):
    return sum([(b**i) for i, num in enumerate(numarr[::-1]) if num == 1])

def get_jamcoins(N, J):
    jc = {}
    bases = xrange(2, 11)

    for numperm in product([0,1], repeat=N-2):
        numarr = [1] + list(numperm) + [1]
        divs = list()
        for b in bases:
            num = get_baserep(numarr, b)
            div = get_divisor(num)
            if div:
                divs.append(div)
            else:
                break
        if len(divs) == len(bases):
            num = ''.join([str(n) for n in numarr])
            facs = ' '.join([str(d) for d in divs])
            yield num, facs

if __name__=='__main__':

    fin = open(argv[1], 'r')
    fin.readline()
    nj = fin.readline().split()
    N, J = int(nj[0]), int(nj[1])
    jcgen = get_jamcoins(N, J)

    fout = open(argv[1]+'_out', 'w')
    fout.write('Case #1:\n')

    i = 0
    while i < J:
        i += 1
        n, f = next(jcgen)
        fout.write('{0} {1}\n'.format(n, f))
    fout.close()
