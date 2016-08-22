#!/bin/python2
import itertools

def isPrime(n,skip=True):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return 2
  if n < 9: return True
  if n%3 == 0: return 3
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return f
    if n%(f+2) == 0: return f+2
    if skip and f>100000:
        return -1
    f +=6
  return True    


def xmain(N,J,lst,skip=True):
    skipped=[]
    print "Case #1:"
    for x in lst:
        if J==0:
            break
        s='1'+''.join(x)+'1'
        divisors=[]
        for b in xrange(2,11):
            r=isPrime(int(s,b),skip)
            if(r==-1):
                skipped.append(s)
                break
            if(r==True):
                break
            else:
                divisors.append(str(r))
        if len(divisors)==9:
            print s,' '.join(divisors)
            J=J-1
    return skipped,J==0


raw_input()
N,J=[int(x) for x in raw_input().split()]
skipped,r=xmain(N,J,itertools.product(['0','1'], repeat=N-2))

if r!=1 and len(skipped)!=0:
    xmain(N,J,skipped,False)