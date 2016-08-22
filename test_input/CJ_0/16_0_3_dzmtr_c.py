import sys
import math

def bin_to_base(x, base):
    p = 1
    y = 0
    for digit in bin(x)[:1:-1]:
        if digit == '1':
            y += p
        p *= base 
    return y

def find_divisor(x):
    if x % 2 == 0:
        return 2
    for i in xrange(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return i
    return -1

sys.stdout.write('Case #1:\n')
count = 0
for i in xrange(1<<14):
    x = 1<<15 | i<<1 | 1;

    divisors = [find_divisor(bin_to_base(x, j)) for j in xrange(3, 11)];
    divisors[:0] = [find_divisor(x)];

    if any(divisor == -1 for divisor in divisors):
        continue

    sys.stdout.write(bin(x)[2:] + ' ' + ' '.join(map(str, divisors)) + '\n')

    count += 1

    if count == 50:
        break
