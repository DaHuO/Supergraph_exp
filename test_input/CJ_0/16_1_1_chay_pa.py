T=int(input())
for t in range(T):
    str=input()
    pev='A'
    a,b=[],[]
    for i in str:
        if i>=pev:
            a.append(i)
            pev=i
        else:
            b.append(i)
    str=''.join(a[::-1]+b[:])
    print('Case #{0}: {1}'.format(t+1,str))
