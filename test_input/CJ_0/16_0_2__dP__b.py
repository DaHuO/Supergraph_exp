def sol(s):
    r = int(s[-1] == '-')
    for i in xrange(1, len(s)):
        r += int(s[i - 1] != s[i])
    return r

rl = lambda: map(int, raw_input().split())

t = input()
for i in xrange(t):
    s = raw_input()
    print "Case #%d:" % (i + 1), sol(s)
