import string

t=int(raw_input())

al=string.uppercase

for _ in range(t):
    s=raw_input().strip()
    res=[]
    used=[False]*len(s)
    first=len(s)
    for c in al[::-1]:
        if s[:first].find(c)==-1:
            continue
        next_first=None
        for i in range(first):
            if s[i]==c:
                used[i]=True
                if None==next_first:
                    next_first=i
                res.append(c)
        first=next_first
    for i in range(len(s)):
        if not used[i]:
            res.append(s[i])
    print "Case #"+str(_+1)+": "+"".join(res)
