T = int(raw_input())
#print T
for x in range(T):
    s = raw_input()
    #print s
    ans = ""
    max_ = 0
    for c in s:
        if ord(c) >= max_:
            max_ = ord(c)
            ans = c + ans
        else:
            ans = ans + c
    print "Case #%s: %s" % (x+1, ans)
