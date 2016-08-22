import sys
for cases in xrange(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    ans = s[0]
    for i in s[1:]:
        if i >= ans[0]:
            ans = i + ans
        else:
            ans += i
    print "Case #%d: %s"%(cases+1,ans)
