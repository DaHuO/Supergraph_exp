a=int(input())
j=0
while j<a:
    j+=1
    b=input()
    A=[]
    for i in b:
        A.append(i)
    a1=[A[0]]
    b1=[]
    f=0
    for i in range(1,len(A)):
        if A[i]<a1[f]:
            b1.append(A[i])
        else:
            a1.append(A[i])
            f+=1
    a1.sort(reverse=True)
    c=''.join(a1)+''.join(b1)
    print("Case #%d: %s" % (j,c))
        
            
