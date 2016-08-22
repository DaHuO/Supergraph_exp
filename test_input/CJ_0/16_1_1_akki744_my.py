t=int(input())
i=1
while(i<=t):
    S=input()
    j=0
    while(j<len(S)):
        if(j==0):
            A=S[j]
        elif(S[j]>=A[0]):
            temp=A
            A=S[j]
            A=A+temp
        else:
            A=A+S[j]
        j+=1
    print("Case #%d: %s"%(i,A))
    i+=1
