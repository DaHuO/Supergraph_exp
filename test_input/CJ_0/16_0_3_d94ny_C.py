import math

def bins(n):
    """Generator for all binary number of length n."""
    return (bin(i)[2:].zfill(n) for i in xrange(2**n - 1))

def nontrivial(n):
    """Returns a non trivial divisor for a number."""
    for i in range(2, int(math.sqrt(n) + 1) + 1):
        if n%i == 0:
            return i
    return 0

def jamcoin(s):
    """Returns non trivial divisor if this is a jamcoin."""
    t = []
    for base in xrange(2, 11):
        x = nontrivial(int(s, base))
        if x != 0:
            t.append(str(x))
        else:
            return []

    return t

t = int(raw_input())
for i in range(t):

    n, j = map(int, raw_input().strip().split(' '))

    print "Case #{0}:".format(i+1)
    for x in bins(n - 2):
        y = jamcoin('1{0}1'.format(x))
        if y:
            print '1{0}1'.format(x),
            print ' '.join(y)
            j -= 1
            if j == 0:
                break
