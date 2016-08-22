def base(num,bas):
    res=0
    val=1
    for i in range(len(num)-1,-1,-1):
         res=res+int(num[i])*val
         val=val*bas
    return res         

def prime(res,primelist):
    for i in primelist:
        if res%i==0:
            return i
    return 0

def translate(value):
    s=''
    while value>0:
         s=s+str(value%2)
         value=value//2
    s=s[::-1]
    return s

T=int(input())
N,J=input().split(' ')
N=int(N)
J=int(J)
print('Case #1:')
value=[0]*11
for i in range(2,11):
    value[i]=i**(N-1)+1
i=1
idx=0
primelist=[2,3,5,7,11,13,17,19,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197]
while i<=J:
    string=translate(idx)
    l='0'*(N-2-len(string))
    result='1'+l+string+'1'
    flag=True
    for j in range(2,11):
        k=value[j]+base(string,j)*j
        judge=prime(k,primelist)
        if judge==0:
            flag=False
            break
        else:
            result=result+' '+str(judge)
    if flag:
        print(result)
        i+=1
    idx+=1
        
