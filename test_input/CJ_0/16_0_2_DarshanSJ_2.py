t=input()
count=1
def rfind(inp,f):
    f=f-1
    while f>=0 and inp[f]=='+':
        f-=1
    return f
while count<=t:
    inp=list(raw_input())
    cur=rfind(inp,len(inp))
    res=0
    while cur>=0:
        temp=0
        if inp[temp]=='+': res+=1
        while inp[temp]=='+':
            inp[temp]='-'
            temp+=1
        #print inp,cur
        res+=1
        next1=list()
        for j in xrange(cur+1):
            next1.append('-' if inp[cur-j]=='+' else '+')
        inp=next1
        #print inp
        cur=rfind(inp,cur)
    print "Case #"+str(count)+": "+str(res)
    count+=1
