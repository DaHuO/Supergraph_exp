b=[]
def form(d,k,l):
    a=[]
    if l<len(d):
        a+form(d,k+d[l],l+1)
        a+form(d,d[l]+k,l+1)
    a.append(k)
    if len(a[0])==len(d):
        b.append(a[0])
    return a

t=int(raw_input())
for o in range(t):
    s=raw_input()
    a=list(s)
    a.sort()
    ex=form(s,s[0],1)
    x=[i for i in b if i[0]==a[-1]]
    x.sort()
    print 'Case #'+str(o+1)+':',x[-1]
    b=[]
