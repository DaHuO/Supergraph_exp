with open("a_in.txt", "r") as f:
    T = int(f.readline().strip())
    for t in xrange(1, T+1):
        s = f.readline().strip()
        ans = list()
        for c in s:
            if len(ans) == 0:
                ans.append(c)
                continue
            if c >= ans[0]:
                ans.insert(0, c)
            else:
                ans.append(c)
        print "Case #%d: %s" % (t, ''.join(ans))
