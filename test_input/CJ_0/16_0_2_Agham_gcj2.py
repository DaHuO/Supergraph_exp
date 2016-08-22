for x in range(int(input())):
    a=input()
    c=1
    temp=a[0]
    for i in range(len(a)):
        if temp!=a[i]:
            c+=1
            temp=a[i]
    if a[len(a)-1]=='-':
        ans=c
    else:
        ans=c-1
    print('Case #'+str(x+1)+': '+str(ans))
