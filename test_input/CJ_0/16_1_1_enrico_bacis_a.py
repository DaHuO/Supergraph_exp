def single(func):
    return func(raw_input())

def row(func):
    return map(func, raw_input().split())

def printcase(case, out, pattern='Case #%d: %s'):
    print pattern % (case, out)

def repeat(func, times):
    return [func() for _ in xrange(times)]


T = single(int)
for t in xrange(1, T + 1):
    first, res = None, ''
    for letter in single(str):
        if first is None or letter >= first:
            res = letter + res
            first = letter
        else:
            res = res + letter
    printcase(t, res)

