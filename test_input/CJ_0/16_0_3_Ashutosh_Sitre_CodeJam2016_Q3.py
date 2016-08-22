import itertools
import sys, traceback
gk=0
def base(c,j):
    ret=0
    for i in range(len(c)):
        ret+=(j**(len(c)-1-i))*c[i]
    return ret

def isPrime(n):
    if n==2 or n==3 or n==1: return 0
    if n%2==0: return 2
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return i    
    return 0

def compute(c):
    bas=[0]*9
    div=[0]*9
    flag=1
    global gk
    for i in range(2,11):
        bas[i-2]=base(c,i)
    for i in range(9):
        if isPrime(bas[i])==0:
            flag=0
            break
        else:
            div[i]=isPrime(bas[i])
    if flag==1:
        if gk>0:
            print "".join(map(str,c))," ".join(map(str,div))
            gk-=1
        else:
            raise SystemExit

def fn(c,i,n):
    if i<1 or i>n-2:
        return
    if i==n-2:
        c[i]=0
        compute(c)
        c[i]=1
        compute(c)
    c[i]=0
    fn(c,i+1,n)
    c[i]=1
    fn(c,i+1,n)
    return

for tc in range(int(raw_input())):
    n,j=map(int,raw_input().split())
    c=[1]
    global gk
    gk=j
    for i in range(n-2):
        c.append(0)
    c.append(1)
    print "Case #" +str(tc+1)+":"
    fn(c,1,n)            
            
            
    
    
