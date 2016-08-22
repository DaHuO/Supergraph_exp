for tc in range(int(raw_input())):
    s=raw_input()
    ans=s[0]
    for i in range(1,len(s)):
        if ord(s[i])>=ord(ans[0]):
            ans=s[i]+ans
        else:
            ans+=s[i]
    print "Case #"+str(tc+1)+": "+ans
