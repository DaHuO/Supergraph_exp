__author__ = 'Devansh-PC'
t=int(input())
cs=1
while t!=0:
    s=input()
    l=list(s)
    nl=[]
    nl.append(s[0])
    for i in range(1,len(l)):
        if l[i]>=nl[0]:
            nl.insert(0,l[i])
        else:
            nl.append(l[i])
    print("Case #"+str(cs)+":",''.join(nl))
    cs+=1