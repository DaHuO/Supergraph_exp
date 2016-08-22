def f(s):
    s=list(s)
    t=s[0]
    for i in range(1,len(s)):
        if t[0]>s[i]:
            t=t+s[i]
        else:
            t=s[i]+t
    return t
t=int(input())
for i in range(t):
    s=input()
    print("Case #%s: %s"%(i+1,f(s)))