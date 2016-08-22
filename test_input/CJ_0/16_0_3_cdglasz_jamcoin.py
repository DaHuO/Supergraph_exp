import itertools
import math

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

binary = lambda k: ('1'+"".join(x)+'1' for x in itertools.product('01', repeat=k-2))

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def is_jamcoin(s):
    divisors = []
    for b in range(2,11):
        x = int(s, b)
        if is_prime(x):
            return []
        divisors.append(divisorGenerator(x).next())
    return divisors




import re

infile = "/Users/Christopher/Downloads/C-small-attempt1.in.txt"
outfile = "/Users/Christopher/Desktop/Python/CodeJam/practice.out.txt"
txt = open(infile)
data = txt.read()
lines = [l for l in re.split('\n+', data) if l][1:]

newlines = []
for i,l in enumerate(lines):
    line = "Case #" + str(i+1) +":\n"
    N, J = [int(x) for x in re.split('\s+', l)]
    j = 0
    for b in binary(N):
        divs = is_jamcoin(b)
        if not divs: continue
        line += b + ' ' + ' '.join(str(d) for d in divs) + '\n'
        j += 1
        if j >= J: break

    newlines.append(line)

lines = '\n'.join(newlines)

target = open(outfile, 'w')
target.write(lines)