from math import sqrt

start = '1'+30*'0'+'1'
stop = 32*'1'

start = int(start,2)
stop = int(stop,2)



def findDivisor(n):
    for i in xrange(2,int(sqrt(n)+1)):
        if n%i == 0:
            return i
    return -1



def firstPrimes(n):
   out = []
   for i in xrange(2,n):
       if findDivisor(i) == -1:
          out.append(i)
   return out

primes = firstPrimes(100000)


def fastFindDivisor(n):
   for p in primes:
      if n%p == 0: return p
   return -1

def isJam(n):
   r = "{0:b}".format(i)
   if r[-1]=='0': return [False]
   out = [True]
   for j in range(2,11):
       p = int(r,j)
       div = fastFindDivisor(p)
       if div == -1 or div==p: return [False]
       out.append(div)
   return out
      


i = start-1
while i<=stop:
   i+=1
   jam = isJam(i)
   if jam[0]:
       print  "{0:b}".format(i) , ' '.join([str(j) for j in jam[1:]])
   



