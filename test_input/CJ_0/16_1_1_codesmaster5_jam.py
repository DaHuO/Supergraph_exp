t=int(raw_input())
for a in range(0,t):
    s=raw_input()
    c=""
    c=c+s[0]
    for i in range(1,len(s)):
        if s[i]>=c[0]:
            c=s[i]+c
        else:
            c=c+s[i]
    print "Case #%d: %s"%(a+1,c)
