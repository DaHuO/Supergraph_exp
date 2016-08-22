import random

def find_divisor(v):
    if v % 2 == 0:
        return 2
    d = 3
    while d < v / 2 and d < 10000:
        if v % d == 0:
            return d
        d += 2

def convert_to_value(s, base):
    p = 0
    v = 0
    while p < len(s):
        v += (base ** p) * s[-p - 1]
        p += 1
    return v

T = int(raw_input().strip())
N, J = [int(item) for item in raw_input().strip().split(' ')]
result = dict()
while len(result) < J:
    s = [1,]
    for i in xrange(N - 2):
        s.append(random.randint(0,1))
    s.append(1)
    val = convert_to_value(s, 10)
    if val in result:
        continue
    r = list()
    for base in xrange(2, 11):
        v = convert_to_value(s, base)
        d = find_divisor(v)
        if d is None:
            break
        r.append(d)
    if len(r) == 9:
        result[val] = r

print 'Case #1:'
for k, v in result.iteritems():
    print k,
    for val in v:
        print val,
    print
