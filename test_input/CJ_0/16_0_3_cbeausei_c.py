import sys

N = 32
J = 500
ntest = 10000

def next():
    t[N - 2] += 1
    k = N - 2
    while t[k] > 1:
        t[k] = 0
        k -= 1
        t[k] += 1
        
def interpret(b):
    v = 0
    for x in t:
        v *= b
        v += x
    return(v)
    
def is_jamcoin():
    val = [interpret(b) for b in range(11)]
    ret = [-1 for b in range(11)]
    left = {}
    for i in range(2, 11):
        left[i] = True
    for k in range(2, ntest):
        to_remove = []
        for x in left:
            if val[x] % k == 0:
                ret[x] = k
                to_remove.append(x)
        for x in to_remove:
            del left[x]
    return((left == {}, ret[2:]))
    
t = [1] + [0] * (N - 2) + [1]

out = 'Case #1:\n'
sys.stdout.write(out)
sys.stdout.flush()
sys.stderr.write(out)
sys.stderr.flush()
j = 0
while j < J:
    bb, div = is_jamcoin()
    if bb:
        j += 1
        out = ''
        for x in t:
            out += str(x)
        for x in div:
            out += ' ' + str(x)
        out += '\n'
        sys.stdout.write(out)
        sys.stdout.flush()
        sys.stderr.write(out)
        sys.stderr.flush()
    next()