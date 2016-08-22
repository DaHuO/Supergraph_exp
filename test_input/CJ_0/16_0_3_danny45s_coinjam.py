from __future__ import print_function
import numpy as np
import sys
a=open(sys.argv[-1]).readlines()
n = int(a[1].split()[0])
j = int(a[1].split()[1])

print('Case #1:')

start = 2**(n - 1) + 1
end = 2**n

count = 0

for i in range(start, end, 2):
    if count >= j:
        break
    vals = []
    factors = []
    for base in range(2, 11):
        vals.append(int(bin(i)[2:], base))
    for num in vals:
        prime = False
        for k in range(2, int(num**(1./16)) + 1):
            if num % k == 0:
                factors.append(k)
                prime = True
                break
        if not prime:
            break
    if len(factors) == 9:
        print(vals[-1], end=' ')
        for factor in factors:
            print(factor, end=' ')
        print()
        count += 1
