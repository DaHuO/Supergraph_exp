import math
import itertools
#also returns true on 0,1 
##def is_prime(n):
##    if n % 2 == 0 and n > 2: 
##        return False
##    for i in range(3, int(math.sqrt(n)) + 1, 2):
##        if n % i == 0:
##            return False
##    return True

##for i in range(100):
##  if (is_prime(i)):
##    print i

def tryNonTrivialDivisor(n):
    if n % 2 == 0 and n > 2: 
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return None


def NonTrivialDivisorsFor2to10Base(strInt):
    res = [strInt]
    for i in range(2,11):
        ans = tryNonTrivialDivisor(int(strInt,i))
        if ans is None:
          return None
        res.append(str(ans))
    #print [int(strInt,i) for i in range(2,11)]
    return res

#give string input
def isNotPrimeFor2To10Base(strInt):
  return not any(is_prime(int(strInt,i)) for i in range(2,11))


def getPossibleJamcoins(N):
  for seq in itertools.product("01", repeat=N-2):
    yield '1'+"".join(seq)+'1'

def getJamcoins(N,J):
  resultCollection = []
  for strInt in getPossibleJamcoins(N):
    res = NonTrivialDivisorsFor2to10Base(strInt)
    if res is None:
      continue #skip because it is prime for at least on base
    resultCollection.append(res)
    if len(resultCollection) == J:
      break
  return resultCollection


def test(strInt):
  #print [int(strInt,i) for i in range(2,11)]

  #print NonTrivialDivisorsFor2to10Base(strInt)
  for i in getPossibleJamcoins(5):
    print i
#test('101')

#test('100011')


def main():
  T = int(input())  # read a line with a single integer
  for i in range(1, T + 1):
    N, J = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    solutionCollection = getJamcoins(N,J)
    print("Case #{}:".format(i))
    for j in solutionCollection:
      print ' '.join(j)



main()


