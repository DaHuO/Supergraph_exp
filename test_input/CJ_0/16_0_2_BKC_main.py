for tc in xrange(input()):
    s = raw_input()
    c = sum([s[i] != s[i+1] for i in xrange(len(s)-1)])
    ans = c + (1 if s[-1] == '-' else 0)
    print "Case #%d: %s" % (tc+1, ans)
