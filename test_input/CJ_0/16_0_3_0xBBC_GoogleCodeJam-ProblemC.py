#coding:utf-8

import math;
import sys;

def is_prime(n):
    if n <= 1:
        return False;
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False;
    return True;
    
def nontrival_divisor(n, exclusive):
    for div in xrange(3, int(math.sqrt(n)) + 1):
        if n % div == 0:
            if div in exclusive:
                continue;
            else:
                return div;
    return 0;

T = int(sys.stdin.readline()[:-1]);
(N, J) = sys.stdin.readline()[:-1].split(' ');
(N, J) = (int(N), int(J))
print('Case #1:')
starts = (1 << (N - 1)) + 1
limits = (1 << N)
found = 0;
for i in xrange(starts, limits, 2):
    if found == J:
        break;
    bin_represent = str(bin(i))[2:]
    base_interprets = []
    for base in xrange(2, 11):
        base_interpret = 0;
        for bit in xrange(0, len(bin_represent)):
            if bin_represent[bit] == '1':
                base_interpret += base ** (len(bin_represent) - bit - 1);
        if is_prime(base_interpret) == False:
            base_interprets.append(base_interpret);
        else:
            break;
    if len(base_interprets) == 9:
        including_trival = False
        result = bin_represent
        for interpret in xrange(0, 9):
#            print(bin_represent, base_interprets[interpret])
            divisor = nontrival_divisor(base_interprets[interpret], base_interprets);
            if divisor != 0:
                result += ' ' + str(divisor)
            else:
                including_trival = True
                break;
        if including_trival == False:
            print(result);
            found += 1;
        
        