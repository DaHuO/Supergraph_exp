import math

n=32
x=500
outf=open("q3large.out","w")

def factor(num):
    r=500
    for i in range(2, r):
        if num%i==0:
            return i
    return -1

def makelist(n):
    lst=[]
    l=len(n)
    for i in range(2, 11):
        num=0
        for j in range(0, l):
            num+=int(n[j])*(i**(l-1-j))
        fac=factor(num)
        if fac==-1:
            break;
        lst.append(fac)
    return lst

def f(n, k):
    if n==0:
        l=makelist(k+"1")
        if len(l)==9:
            outf.write(k+"1")
            for p in l:
                outf.write(" "+str(p))
            outf.write("\n")
            global x
            x=x-1
            print(x)
            if x==0:
                outf.close()
                exit()
    else:
        f(n-1, k+"0")
        f(n-1, k+"1")
        
f(n-2, "1")