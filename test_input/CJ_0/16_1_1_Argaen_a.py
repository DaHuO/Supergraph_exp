
def solve(s):
    r = ''
    for c in s:
        if len(r) == 0 or c >= r[0]:
            r = c + r
        else:
            r += c
    return r


T = int(raw_input())
i = 1
while i <= T:
    s = raw_input()
    print 'Case #{0}: {1}'.format(i, solve(s))
    i += 1

