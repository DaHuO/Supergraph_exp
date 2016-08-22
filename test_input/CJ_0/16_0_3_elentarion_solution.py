import math
import numpy as np
import sys

nb_test_cases = int(raw_input())
print 'Case #%d:' % (nb_test_cases)

n, j = map(int, raw_input().split())

def is_prime(min, max, n):
    if n % 2 == 0 and n > 2: 
        return 2

    for i in xrange(min, max, 2):
        if n % i == 0:
            return i

    return 0

min = 3
max = 10000
i = 2**(n-1) + 1
count = 0
while count < j:
    binary_digits = str(bin(i))[2:]

    if len(binary_digits) == n and binary_digits[0] == '1' and binary_digits[len(binary_digits) - 1] == '1':
        proofs = []
        found = True
        for base in range(2, 11):
            proof = is_prime(min, max, int(binary_digits, base))
            if proof == 0:
                found = False
                break
            else:
                proofs.append(proof)

        if found:
            count += 1
            print '%s %s' % (binary_digits, ' '.join([ str(proof) for proof in proofs]))
            sys.stdout.flush()
    elif len(binary_digits) > n:
        break

    i += 1