import math
from pyecm import factors # pyecm

def get_one_factor(n):
    for x in factors(n, False, False, 2 * math.log(math.log(n)), 1.0):
        return x

print 'Case #1:'
raw_input()
n, j = map(int, raw_input().strip().split())
for i in xrange((1 << (n - 1)) + 1, 1 << n, 2):
    s = bin(i)[2:]
    fs = []
    for base in xrange(2, 11):
        n_in_base = int(s, base)
        f = get_one_factor(n_in_base)
        if f == n_in_base:
            break
        fs.append(f)
    if len(fs) == 9:
        print '%s %s' % (s, ' '.join(map(str, fs)))
        j -= 1
    if not j: break
