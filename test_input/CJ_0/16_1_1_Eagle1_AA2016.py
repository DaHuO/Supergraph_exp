T=int(input())
for t in range(0,T):
    S=input()
    B=S[0]
    for s in range(1,len(S)):
        if S[s]>=B[0]:
            B=S[s]+B
        else:
            B=B+S[s]
    print("Case #%d: %s"%(t+1,B))
