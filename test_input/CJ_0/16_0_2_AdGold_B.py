def solve(s):
    s = s.strip()
    res = 0
    for i in range(1, len(s)):
        res += (s[i-1] != s[i])
    res += s[-1] == '-'
    return res

#  inp = list(open('b-sample.in'))[1:]
#  inp = list(open('B-small-attempt0.in'))[1:]
inp = list(open('B-large.in'))[1:]
for t, s in enumerate(inp):
    print 'Case #%d: %s' % (t+1, solve(s))
