from math import sqrt
def itb(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return itb(n//base,base) + convertString[n%base]
def getdiv(n):
    n=int(n)
    if n%2==0:
        return 2
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0:
            return i
    return -1
def f(n,j):
    l=[]
    div=[]
    for i in range(2**n):
        d=[]
        s=itb(i,2)
        while len(s)<n:
            s="0"+s
        s="1"+s+"1"
        for k in range(2,11):
            if getdiv(int(s,k))!=-1:
                d.append(getdiv(int(s,k)))
        if len(d)==9:
            l.append(s)
            div.append(d)
        if len(l)==j:
            break
    for i in range(j):
        s=l[i]+" "+" ".join(str(k) for k in div[i])
        print (s)

t=int(input())
n,j=map(int,input().split())
n-=2
f(14,50)