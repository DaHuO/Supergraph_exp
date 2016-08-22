Tc=int(input())
for t in range(1,Tc+1):
    S=input()
    ans=None
    for c in S:
        if(not ans):
            ans=c
            continue
        if (c >= ans[0]):
            ans=c+ans
        else:
            ans=ans+c
    print("Case #{0}: {1}".format(t,ans))