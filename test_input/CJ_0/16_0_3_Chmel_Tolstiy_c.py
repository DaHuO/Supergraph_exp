import sys

N = 32
T = 500

print "Case #1:"

for i in xrange(T):
    x = 1 + i*2 + (1 << (N / 2)) / 2
    d = bin(x)[2:]
    s = d + d
    print " ".join([s] + map(str, map(lambda x: int(d, x), xrange(2, 11))))
    