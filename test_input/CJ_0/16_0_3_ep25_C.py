import sys

MAX_PRIME = 3
PRIME_NUM_SET = set([2, 3])

def checkIfPrime(n):
    """Returns True if n is prime.
    
    Stolen from: http://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime
    
    Modified to return smallest prime factor if not prime
    """
    global MAX_PRIME
    global PRIME_NUM_SET

    # if MAX_PRIME:
    if n <= MAX_PRIME and (n in PRIME_NUM_SET):
        return True, None

    # if n == 2:
    #     if n > MAX_PRIME:
    #         MAX_PRIME = n
    #     PRIME_NUM_SET.insert(2)
    #     return True, None
    # if n == 3:
    #     if n > MAX_PRIME:
    #         MAX_PRIME = n
    #     PRIME_NUM_SET.insert(3)
    #     return True, None
    if n % 2 == 0:
        return False, 2
    if n % 3 == 0:
        return False, 3

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False, i

        i += w
        w = 6 - w

    if n > MAX_PRIME:
        MAX_PRIME = n
    PRIME_NUM_SET.add(n)
    return True, None


def convertToDecimal(num, base):
    """ 
    num: List of 1s and 0s
    base: int
    """
    result = 0
    
    power = 0
    for digit in reversed(num):
        result += digit * (base**power)
        power += 1
        
    return result


def convertToVariousBases(bitStr):
    for b in range(2, 11):
        yield convertToDecimal(bitStr, b)

def generateBinStrings(length):
    for i in range(0, 2**length):
        yield [1 if digit=='1' else 0 for digit in bin(i)[2:].zfill(length)]


def generatePossibleJamCoins(N):
    for bitStr in generateBinStrings(N-2):
        lstBitStr = [1]
        lstBitStr.extend(bitStr)
        lstBitStr.append(1)
        yield lstBitStr


def checkIfJamCoin(bitStr):
    smallestPrimeDivisors = []
    for d in convertToVariousBases(bitStr):
        isPrime, smallestDivisor = checkIfPrime(d)
        if isPrime:
            return False, None
        else:
            smallestPrimeDivisors.append(smallestDivisor)  

    assert len(smallestPrimeDivisors) == 9 
    return True, smallestPrimeDivisors

def convertBitStrToString(bitStr):
    result = ""
    for bit in bitStr:
        result += str(bit)
    
    return result

def main():
    ln = 0
    T = None
    for line in sys.stdin:
        if ln == 0:
            T = int(line)
            ln += 1
        else:
            inStr = line.rstrip().split()
            N, J = int(inStr[0]), int(inStr[1])
            print("Case #{0}:".format(ln))

            for bitStr in generatePossibleJamCoins(N):
                if J == 0:
                    break

                isJamCoin, divisors = checkIfJamCoin(bitStr)
                if isJamCoin:
                    outStr = convertBitStrToString(bitStr)
                    for d in divisors:
                        outStr += " {0}".format(d)
                    print(outStr)

                    J = J - 1
            ln += 1


if __name__ == '__main__':
    main()
