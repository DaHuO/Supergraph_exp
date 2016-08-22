session = 'C-large'

filename_in = session + '.in'
filename_out = session + '.out'

from math import sqrt
from itertools import count, islice
import time

def isPrime(n):
    now = time.time()
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if number % 100:
            if time.time() - now > 0.01:
                return -1
        if not n%number:
            return number
    return -1

def check_jamcoin(x):
    div_array = []
    
    for b in range(2, 11):
        num = int(x, b)
        div = isPrime(num)
        if div == -1:
            return -1
        else:
            div_array.append(div)
        div_array = map(str, div_array)
    return x + ' ' + ' '.join(div_array)
    
    pass

def get_bin(x, L):
    y = bin(x)[2:]
    y = '1' + '0'*(L - len(y)) + y + '1'
    return y
    
def solve_case(N, J):
    K = 2**(N-2)
    
    ret = []
    i = 0
    while len(ret) < J:
        print len(ret)
        x = get_bin(i, N-2)
        cur = check_jamcoin(x)
        if cur != -1:
            ret.append(cur)
        i += 1
        
    
    return ret


with open(filename_in) as fin, \
    open(filename_out, 'wb') as fout:
    now = time.time()
    T = int(fin.readline().strip())
    print T
    for i in range(1, T+1):
        N, J = map(int, fin.readline().strip().split())
        y = solve_case(N, J)
        fout.write('Case #%d:\n' % i)
        for line in y:
            fout.write(line + '\n')
    
    print "time elapsed", (time.time() - now)/60
