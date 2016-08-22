from sys import stdin as ip
from math import factorial as fff
from fractions import gcd
from itertools import combinations as c
f=pow(2,3,3)
xs=fff(f+2)
author='biggy_bs'
# Main code goes here !!
dp=[0]*110
val_dic={}
def factors(n):    
    l=[]
    for i in range(2, 1000):
        q,r = n/i, n%i     
        if r == 0:
            l.append(i) 
    return l
def divisor(x):
    for i in range(2,n):
        if x%i==0:
            return i
def primes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in xrange(int(limit**0.5 + 1.5)): 
        if is_prime[n]:
            for i in range(n * n, limit + 1, n): 
                is_prime[i] = False
    for i in xrange(limit + 1):
        if is_prime[i]: yield i
xxa=list(primes_upto(10000))
primes={}
dic={}
def gen(pos,n,cur,j):
    if pos>n:
        return
    if len(dic)==j:
        return
    if len(cur)==n:
        if not ok(cur):
            return
    gen(pos+1,n,cur+'0',j)
    gen(pos+1,n,cur+'1',j)

def ok(s):
    s='1'+s+'1'
    dic[s]=[]
    for i in xrange(2,11):
        c=int(s,i)
        fac=factors(c)
        if fac==[]:
            del dic[s]
            return False
        else:
            dic[s].append(fac[0])
    else:
        return True

f=open('op2.txt',"w")
for _ in xrange(int(ip.readline())):
    n,j=map(int,ip.readline().split())
    n=50
    gen(0,48,'',j)
    f.write("Case #%d:\n"%(_+1))
    for i in dic:
        f.write(str(i)+" ")
        for j in dic[i]:
            f.write(str(j)+" ")
        f.write("\n")
f.close()
