import random
v=[]
def val(str,base):
    ct=0
    ans=0
    for i in reversed(str):
        if i=='1':
            ans=ans+base**ct
        ct=ct+1
    return ans
def isprime(a):
    for i in v:
        if i>=v:
            return 0
        if a%i==0:
            return i
    return 0
p=[0]*100001
MAX=1000
for i in range(2,MAX):
    if p[i]==0:
        for j in range(2,MAX):
            if(i*j>=MAX):
                break
            else:
                p[i*j]=1
for i in range(2,MAX):
    if p[i]==0:
        v.append(i)
n,mx=map(int,raw_input().split(' '))
mans=0
mylist=[]
print "Case #1:"
while 1:
    if mans==mx:
        break
    ans=[]
    flag=0
    stg='1'
    for i in range(0,n-2):
        x=random.randrange(0,1023)
        if x%2==1:
            stg+='1'
        else:
            stg+='0'
    stg+='1'
    if stg not in mylist:
        mylist.append(str)
    else:
        continue
    for i in range(2,11):
        j=isprime(val(stg,i))
        if j == 0:
            flag=1
        else:
            ans.append(j)

    if flag==0 :
        mans=mans+1
        trail=' '.join(map(str,ans))
        stg = stg+' '+trail
        print stg



