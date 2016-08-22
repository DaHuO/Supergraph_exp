Tc=int(input())
for t in range(1,Tc+1):
    ps=input()
    last=None
    top=None
    ans=None
    c=0
    for p in ps:
        if last==p:
            continue;
        last=p 
        if not top:
            top=p
        c+=1;
    if top=='+':
        if c%2:
          ans=c-1
        else:
          ans=c
    else:
        if c%2:
            ans=c
        else:
            ans=c-1
    print("Case #{0}: {1}".format(t,ans))