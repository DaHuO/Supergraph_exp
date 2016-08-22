#!/bin/python
import sys
import numpy as np
from numba import jit
def next_binary(n):
    for i in range(1 << n):
        yield bin(i)[2:].zfill(n)
@jit
def find_divisor(n):
    for i in range(2, int(np.sqrt(n)+1)):
        if n % i == 0: 
            return i
    return 1

if __name__ == '__main__':
    input_name = sys.argv[1] 
    output_name = sys.argv[2] if len(sys.argv) > 2 else input_name.split('.')[0] + '.out'
    f = open(input_name, 'r')
    f2 = open(output_name, 'w')
    nb_cases = int(f.readline().strip())
    for i in range(1, nb_cases+1):
        print 'case ' + str(i)
        f2.write('Case #' + str(i) + ':\n') 
        N, J = map(int, f.readline().strip().split(' '))
        next_bin = next_binary(N - 2)
        nb_jamcoin = 0
        while nb_jamcoin < J: 
            tmp = next_bin.next()
            tmp = '1' + tmp + '1'
            lst = map(lambda x: int(tmp, x), range(2, 11))
            lst = map(lambda x: find_divisor(x), lst)
            is_not_prime = map(lambda x: x != 1, lst)
            if all(is_not_prime):
                nb_jamcoin += 1
                f2.write(tmp + ' ')
                map(lambda x: f2.write(str(x) + ' '), lst)
                f2.write('\n')
    f.close()
    f2.close()
