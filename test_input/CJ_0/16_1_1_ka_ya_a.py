def solve(s):
    res = s[0]
    s = s[1:]

    for c in s:
        st = c + res
        sl = res + c
        if st < sl:
            res = sl
        else:
            res = st

    return res


T = input()
for i in xrange(1, T+1):
    S = raw_input()
    print 'Case #{}: {}'.format(i, solve(S))
