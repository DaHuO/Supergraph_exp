
# coding: utf-8

# In[1]:

def primes(n): # sieve of eratosthenes by http://stackoverflow.com/users/448810/user448810
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
           ps.append(p)
           for i in range(p * p, n + 1, p):
               sieve[i] = False
    return ps

def findFactor(n,listPrimes): #find a factor of non-prime number
    for i in listPrimes:
        if n % i == 0:
            return i
    return 'ERROR'
        
def allBases (n,listBases): #Return the value of n in bases 2 to 10
    ori = list("{0:b}".format(n))
    sumBases = [0 for i in listBases]
    for i in range(len(ori)):
        tempD = ori.pop()
        if tempD == '1':
            cBase = [pow(x,i) for x in listBases]
            for j in range(len(sumBases)):
                sumBases[j] = sumBases[j] + cBase[j]
    return sumBases
                
def formatOutput (curN,N): #Fits the output string of the selected jamcoin to N bits
    curStr = "{0:b}".format(curN)
    for i in range(N-len(curStr)):
        curStr = '0' + curStr
    return curStr


# In[2]:

f = open('input.in','r')
f.readline()
N,J = [int (x) for x in (f.readline().split())]
f.close()
listPrimes = (primes(pow(2,16)+1))
listBases = list(range(2,11))
listPrimesSet = set(listPrimes)
listPrimes.sort()
o = open('Ex2S.out','w')
o.write('Case #1:\n')


# In[3]:

counter = 0
for curN in range(pow(2,N-1)+1,pow(10,N)+1,2):
    toCheck = allBases(curN,listBases)
    if len(listPrimesSet.intersection(set(toCheck))) == 0:
        rr = ([findFactor(x,listPrimes) for x in toCheck])
        if not 'ERROR' in rr:
            o.write(formatOutput(curN,N))
            [o.write(" " + str(x)) for x in rr]
            o.write("\n")
            counter = counter + 1
            if counter >= J:
                break
o.close()

