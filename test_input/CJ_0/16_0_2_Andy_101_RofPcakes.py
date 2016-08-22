t=input()
for ii in range(1,t+1):
    s=raw_input()
    c=0
    for i in range(0,len(s)-1):
        if s[i]!=s[i+1]:
            c=c+1
    if s[len(s)-1]=="-":
        c=c+1
    print "Case #%d: %d"%(ii,c)
