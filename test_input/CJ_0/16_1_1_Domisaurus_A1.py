t = int(raw_input())
for j in xrange(1,t+1):
    s = list(raw_input())
    n = len(s)
    ans = s[0]
    for i in xrange(1,n) :
    	if ord(s[i]) >= ord(ans[0]):
    		ans = s[i] + ans
    	else:
    		ans += s[i]
    print "Case #{}: {}".format(j,ans)