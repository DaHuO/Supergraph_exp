t = int(raw_input())  # read a line with a single integer
for j in xrange(1, t + 1):
    s=raw_input()
    ans=s[0]
#    n, d = [int(x) for x in raw_input().split(" ")] 
    for i in xrange(1,len(s)):
        if(ans[0]>s[i]):
            ans=ans+s[i]
        else:
            ans=s[i]+ans
    print "Case #{}: {}".format(j, ans)
