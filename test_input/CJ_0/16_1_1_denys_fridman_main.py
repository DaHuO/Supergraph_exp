def solve(s):
    n = len(s)
    ans = s[0]
    for i in xrange(1, n):
        if s[i] >= ans[0]:
            ans = s[i] + ans
        else:
            ans += s[i]
    return ans


for qq in xrange(1, int(raw_input()) + 1):
    ans = solve(raw_input())
    print 'Case #%d: %s' % (qq, ans)
