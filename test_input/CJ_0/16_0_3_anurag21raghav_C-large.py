import random
import math
def check_prime(x):
    i = 2
    while(i*i<x):
        if(x%i==0):
            return i
        i+=1
    return -1
Ans=[]
a=""
while(len(Ans)!=500):
    li=['0', '1']
    a=""
    for i in xrange(1, 33):
        if(i==1 or i==32):
            a+='1'
        else:
            a+=li[random.randint(0, 1)]
    b=list(a)
    b=b[::-1]
    temp=[]
    flag = False
    for i in xrange(2, 11):
        ans=0
        for j in xrange(len(b)):
            ans+=(i*int(b[j]))**j
        q=check_prime(ans)
        if(q==-1):
            flag = True
            break
        else:
            temp.append(q)
    if(flag):
        continue
    print a,
    for i in temp:
        print i,
    print
for i in Ans:
    print i[0],
    for j in i[1]:
        print j,
    print