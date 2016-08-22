def f(s):
    count=0
    if '-' not in s:
        return count
    ch=s[0]
    for i in range(1,len(s)):
        if s[i]!=ch:
            ch=s[i]
            count+=1
    if s[-1]=='+':
        count-=1
    return count+1
t=int(input())
for i in range(t):
    n=input()
    print ("Case #%s: %s"%(str(i+1),str(f(n))))
