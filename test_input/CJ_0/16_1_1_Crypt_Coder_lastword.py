test=int(raw_input())
ti=0
while(test):
    test-=1
    ti+=1
    s=raw_input()
    ans=""
    length=len(s)
    ans=s[0]
    for i in xrange(1,length):
        if(ord(s[i])>=ord(ans[0])):
            ans=s[i]+ans
        else:
            ans=ans+s[i]
    st="Case #"+str(ti)+":"
    print st,
    print ans
