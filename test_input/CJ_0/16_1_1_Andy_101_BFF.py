t=input()
for ij in xrange(0,t):
    s=raw_input()
    p=s[0]
    for i in xrange(1,len(s)):
        if s[i]>=p[0]:
            p=s[i]+p
        else:
            p=p+s[i]
    print("CASE #%d: %s"%(ij+1,p))
    p=""
    
    
