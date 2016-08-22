import time, itertools,math
trials = 100000000

def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

infilename ='in.txt'

primes = rwh_primes2(10000000)
timestart = time.time()
iterations = 0
problem = []

def bank (size):
    bank = []
    coin = '1'
    tempstr = ''
    for i in itertools.product([0,1],repeat=size):
        for digit in i:
            tempstr += str(digit)
        coin += tempstr
        coin += '1'
        bank.append(coin)
        coin,tempstr = '1',''
    return bank


def getPowers(coin):
    powerArray = []
    total =0
    for i in range(2,11):
        # print str(i) + "power",
        size = len(coin)
        for digits in range(0,size):
            total += int(math.pow(i,(digits))*int(coin[size-digits-1]))
            #print math.pow(i,(digits)),int(coin[size-digits-1])
            # print total
        powerArray.append(total)
        # print total,
        # if isPrime(total):
        #     print "Prime!",
        total = 0
    return powerArray
def getLeastFactor(power):
    # primes = rwh_primes2(100)
    # primes = primes[::-1]
    for i in primes:
        if i>=2:
            if power%i==0:
                return i



def getLeastFactors(coins):
    newCoins = dict()
    for i in coins:
        newArray = []
        print i,coins[i]
        for j in coins[i]:
            newArray.append( getLeastFactor(j))
        newCoins[i]= newArray
    return newCoins




def solve(coins):
    numValCoins = 0
    validCoins = dict()
    print  coins
    withdraw = bank(int(coins[0])-2)
    print "max coins"+coins[1]
    #withdraw = bank(4-2)
    print withdraw
    for i in withdraw:
        valid = True
        print "working on coin:"+i
        powers = getPowers(i)
        for i in powers:
            if isPrime(i):
                valid = False
        if valid:
            validCoins[i]=powers
            numValCoins += 1
            print numValCoins
        if numValCoins >= int(coins[1]):
            break
    # print validCoins
    print int(coins[1])
    validMimimumCoins = getLeastFactors(validCoins)
    return validMimimumCoins



f = open(infilename, 'r')
iterations = int(f.readline())
for i in range(0,iterations):
    # print i
    problem.append( f.readline().strip().split(' ') )
fw = open('out.txt', 'w')
num = 1
counter = 0
for i in problem:
    answer=solve(i)
    print "Case #"+str(num)+": \n"
    fw.writelines("Case #"+str(num)+": \n")
    outstr = ""
    print answer
    for i in answer:
        print i,
        outstr += str(i)
        for j in answer[i]:
            outstr += " "+str(j)
            print j,
        print
        print "*"+outstr
        fw.writelines(outstr+"\n")
        counter+=1

        # print problem[0][1]
        if counter >= int(problem[0][1]):
            print "done!"

            break
        outstr = ""
    #fw.writelines("Case #"+str(num)+": "+answer+"\n")
    num += 1



print time.time()-timestart





