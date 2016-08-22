import sys, string, random

def check_prime(n):
    x=2
    while x*x<=n and x<=1000:
        if n%x==0: return x
        x+=1
    return 0
    
def to_num(l,base):
    x=0
    for e in l:
        x=x*base+e
    return x

t=int(raw_input())
for gdsge in xrange(t):
    n,j=map(int,raw_input().split())
    s=set()
    while len(s)<j:
        l=[random.randint(0,1) for r in xrange(n)]
        l[0]=1
        l[n-1]=1
        ok=1
        for d in range(2,11):
            if check_prime(to_num(l,d))==0:
                ok=0
        if ok:
            s.add(tuple(l))
            
print "Case #1:"
for e in s:
    l=list(e)
    s=""
    for x in l:
        s+=str(x)
    sys.stdout.write(s+" ")
    for d in range(2,11):
        sys.stdout.write(str(check_prime(to_num(l,d)))+" ")
    sys.stdout.write("\n")
    
    