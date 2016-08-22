import sys
import math

"""
@author Daniel Flores
@date 9/04/2016
"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def getNumberValueInBase(n, base):
    result = 0
    #digits = int(math.log10(number))+1
    digits = list(map(int, str(n)))
    for i in range(0, len(digits)):
        result += digits[ len(digits) - i - 1] * base**i
    return result

def countPrimes(n):
    # Create an array with length n
    isPrime = [True] * n

    # Loop's ending condition is i*i < n, instead of i < sqrt(n)
    # to avoid repeatdly calling an expensive function sqrt
    for i in range(2, n):
        if i*i >= n: break
        if not isPrime[i]: continue
        for j in range(i**2, n, i):
            isPrime[j] = False

    # Now, let's count the primes numbers
    count = 0
    primes = []
    for i in range(2, n):
        if isPrime[i]:
            primes.append(i)
            count+=1

    return primes

def checkPrimeAndReturnLastDivisor(n):
    if n<=1: return False
    #x = math.sqrt(n)
    i = 2
    while i <= n:
        if i**2 > n: break
        if n % i == 0:
            return (False, i)
        i+=1
    return (True, -1)

def checkPrime(n):
    if n<=1: return False
    #x = math.sqrt(n)
    i = 2
    while i <= n:
        if i**2 > n: break
        if n % i == 0:
            return False
        i+=1
    return True

def toBase(base, number):
    digits = "0123456789ABCDEF"
    remStack = Stack()
    while number > 0:
        remainder = number % base
        remStack.push(remainder)
        number = number // base

    newString = ""
    while not remStack.isEmpty():
        newString = newString + digits[remStack.pop()]

    return newString

def getNonTrivialDivisor(n):
    for i in range(2, n):
        if(n % i == 0): return i
    return n

def getNonTrivialDivisorInAllBases(n):
    # n is in base 10
    a = []
    for i in range(2, 11):
        number = getNumberValueInBase(n, i)
        a.append(getNonTrivialDivisor(number))
    return a

def CoinJam(N, J):
    # QUANTITY = J
    # LENGTH = N

    _min = 2**(N-1) + 1
    _max = 2**N - 1

    valids = []
    j = 0

    print("min : ", _min)
    print("max : ", _max)

    numbers = []

    """
    i = _min
    while i <= _max:
    #for i in range(_min, _max + 1):
        binary = int(toBase(2,i))
        if not checkPrime(i):
            for base in range(3, 11):
                #print("binary ==> ", binary)
                number = getNumberValueInBase(binary, base)
                isPrime = checkPrime(number)
                #print(binary, " value in base ", base, " ==> ", number , " is prime ? ", isPrime)
            if not isPrime:
                numbers.append(binary)
            if len(numbers) == J:
                break
        i+=1
    """


    i = _min
    while i <= _max:
    #for i in range(_min, _max + 1):
        binary = toBase(2,i)
        if binary[15] == '1':
            binary = int(binary)
            if not checkPrime(i):
                nonTrivialDivisors = []
                for base in range(2, 11):
                    #print("binary ==> ", binary)
                    number = getNumberValueInBase(binary, base)
                    isPrime, lastDivisor = checkPrimeAndReturnLastDivisor(number)
                    if isPrime: break
                    nonTrivialDivisors.append(lastDivisor)
                    #print(binary, " value in base ", base, " ==> ", number , " is prime ? ", isPrime)
                if not isPrime:
                    numbers.append([binary] + nonTrivialDivisors)

        if len(numbers) == J:
            break

        i+=1


    #print("Numbers : ", numbers)
    #print("Numbers : ", len(numbers))
    return numbers

if __name__ == '__main__':
    #available_numbers = 2**16 - len(countPrimes(2**16))
    #print(available_numbers)

    f = open('output', 'w')
    N = 16
    J = 50
    numbers = CoinJam(N, J)
    print("Case #1:", file=f)
    for i in numbers:
        #result = [i] + getNonTrivialDivisorInAllBases(i)
        print(*i, sep=" ", file=f)
