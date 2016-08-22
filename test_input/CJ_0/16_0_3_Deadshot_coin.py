import math
l = []
i = 2**15+1
while(i<=2**16):
    l.append(i)
    i+=2
w = open("outputcoin.txt","w")
def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True
'''def isprime(a):
    return all(a % i for i in xrange(2, a))'''
'''def isprime(n):
    myList = []
    for i in range(2, n):
        if n % i == 0:
            myList.append(i)
    return myList'''
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)))
'''def getp(integer, start=4):
  primes = [2,3]
  for num in range(start, integer):
    if integer % num == 0:
      for i, prime in enumerate(primes):
        if num % prime == 0:
          break
        if i >= len(primes) - 1:
          primes.append(num)

  return primes'''
def baseN(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
w.write("Case #1:")
count = 50
for i in range(0,len(l)):
    r = []
    flag = 0
    reslist = []
    for j in range (2,11):
        res = int(bin(l[i])[2:],j)
        #r.append(res)
        #print res,"------"
        if isprime(res) == True:
            flag = 1
            break
            print "hello"
        else:
            reslist.append(res)
    if flag == 0:
        for j in range(0,len(reslist)):
            res = reslist[j]
            rn = factors(res)
            r.append(rn.pop())
        print bin(l[i])[2:],
        w.write(str(bin(l[i])[2:])+" ")
        for k in range(0,len(r)):
            print r[k],
            w.write(str(r[k])+" ")
        count-=1
        print ""
        w.write("\n")
    if count == 0:
        break
w.close()
    
