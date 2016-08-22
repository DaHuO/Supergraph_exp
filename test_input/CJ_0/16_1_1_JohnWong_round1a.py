fn = "sample.in"
debug = False

def process(num, S):
    r = [S[0]]
    for x in range(1, len(S)):
        if S[x] >= r[0]:
            r.insert(0, S[x])
        else:
            r.append(S[x])
    print('Case #' + str(num) + ': ' + ''.join(r))

with open(fn) as f:
    n = int(f.readline()[:-1])
    if debug:
        print('count: ' + n)
    for i in range(1, n + 1):
        line = f.readline()[:-1]
        process(i, line)
        pass
    print
    pass

