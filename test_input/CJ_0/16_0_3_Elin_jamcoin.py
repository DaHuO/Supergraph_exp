import string, math
digs = string.digits + string.letters

def int2base(x, base):
    if x < 0: sign = -1
    elif x == 0: return digs[0]
    else: sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[x % base])
        x /= base
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)

from fractions import gcd
import random

def brent(N):
        if N%2==0:
            return 2
        y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
        g,r,q = 1,1,1
        while g==1:             
            x = y
            for i in range(r):
                y = ((y*y)%N+c)%N
            k = 0
            while (k<r and g==1):
                ys = y
                for i in range(min(m,r-k)):
                    y = ((y*y)%N+c)%N
                    q = q*(abs(x-y))%N
                g = gcd(q,N)
                k = k + m
            r = r*2
        if g==N:
            while True:
                ys = ((ys*ys)%N+c)%N
                g = gcd(abs(x-ys),N)
                if g>1:
                    break
         
        return g   

from sympy.ntheory import pollard_pm1, primefactors
def pollard(n):
    return pollard_pm1(n) or n

def plite_number(n):
    # for i in xrange(2, int(n ** .5) , 1):
    #     if (n % i) == 0:
    #         return i
    return pollard(n)

def gen_base_num(jam):
    return [int(int2base(int(jam, base), 10)) for base in xrange(2, 11, 1)]

def gen_jamcoin(length, find_count):
    l = length - 1
    s = 2 ** length
    jams = []
    for c in xrange((2147488539) + 1, s, 1):
        jam = bin(c)[2:]
        if len(jams) < find_count and jam[len(jam) - 1] != '0':
            basesNum = gen_base_num(jam)
            valid = True
            for i in xrange(len(basesNum)):
                num = plite_number(basesNum[i])
                if num == 1 or num == basesNum[i]:
                    valid = False
                    break
                else:
                    basesNum[i] = int(num)
            if valid:
                print jam, basesNum, len(jams)/float(find_count) * 100, '%'
                jams.append((jam, basesNum))
            if len(jams)/float(find_count) > 0.998:
                break
    return jams

def load_input(filename = None):
    if not filename:
        return
    line_buffer = None
    with open(filename, 'r+') as f:
        line_buffer = f.read().splitlines()
    f.close()
    return line_buffer

import sys  

def main(argv):
    if not argv:
        filename = __file__
        lines = ['1', '16 3']
    else:
        filename = argv[0]
        lines = load_input(filename + '.in')
    f = open(filename + '.out', 'w+')
    for i in xrange(int(lines[0])):
        N, J = map(str, lines[i + 1].split(' '))
        jamcoins = gen_jamcoin(int(N), int(J))
        s =  'Case #%d:\n'%(i+1)
        if jamcoins:
            for j in xrange(len(jamcoins)):
                s += ('%s %s\n' % (jamcoins[j][0], ' '.join(str(jam) for jam in jamcoins[j][1])))
        f.writelines(s)
        print '%s'%s
    f.close()

if __name__ == '__main__':
    main(sys.argv[1:])