def openFile():
    f = open("/Users/bosley/Downloads/B-small-attempt0.in")
    lines = [x.rstrip() for x in f.readlines()]
    n = int(lines[0])
    return n, lines

def go(n, lines):
    f = open("/Users/bosley/Desktop/B.out",'w')
    for i in range(0, n):
        v = lines[i+1]
        s = solve(v)
        solnstr = 'Case #{}: {}\n'.format(i+1, s)
        f.write(solnstr)
        print solnstr,

def match(v):
    for i in range(0, len(v)):
        if v[i] != '+':
            return False
    return True

def flip(v, m, n):
    v2 = ['?'] * n
    for i in range(0, m):
        if v[m-1-i] == '+':
            v2[i] = '-'
        else:
            v2[i] = '+'
    for i in range(m, n):
        v2[i] = v[i]
    #print '{} =>_{} {}'.format(v, m, ''.join(v2))
    return ''.join(v2)

def solve(v):
    n = len(v)
    if match(v):
        return 0
    queue = {v : 0}
    i = 0
    while True:
        i += 1
        elems = [(s, v) for s, v in queue.iteritems() if v == i-1]
        #print queue
        for s, k in elems:
            for j in range(1, n+1):
                f = flip(s, j, n)
                if match(f):
                    return i
                if f not in queue:
                    queue[f] = i        

n, lines = openFile()
go(n, lines)
