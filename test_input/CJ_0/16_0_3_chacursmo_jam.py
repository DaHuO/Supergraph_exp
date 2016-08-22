#!/usr/local/bin/python





f = open("C-small-attempt1 (1).in", "rb")
T = int(f.readline())

def main():
    for line in range(T):
        gong = f.readline()
        gong = gong.split(" ")
        N = int(gong[0])
        J = int(gong[1])
    result = []
    c = generateCoin(N,J)
    print "Case #1:"
    oftherealm = c[0]
    digifers = c[1]

    for i in range(J):
        print oftherealm[i],
        for moo in digifers[i]:
            print moo,
        print ""

def ditto(n):
    result = []
    for base in range(2,11):
        temp = n
        tempRes = 0
        i = 0
        while not (temp == 0):
            rem = temp % 10
            tempRes += rem * pow(base,i)
            temp/=10
            i +=1
        result.append(myFactor(tempRes))
    return result

def myFactor(numb):
    from math import log
    from math import sqrt
    poboy = int(round(log(numb)))
    maximillius = int(round(sqrt(numb)))
    for i in range(poboy,maximillius,poboy):
        if (numb % i) == 0:
            return i
        if (numb % (i+1)) == 0:
            return (i + 1)
        if (numb % (i-1)) == 0:
            return (i - 1)


def fermatDivisor(num):
    print num
    from math import sqrt,ceil
    a = int(ceil(sqrt(num)))
    b2 = a*a - num
    i = 3
    while not isSquare(b2):
        if (num%i) == 0:
            return i
        i+=2
        a += 1
        b2 = a*a-num
    temp = a - sqrt(b2)
    return int(temp)

def isSquare(num):
    ntemp = num
    rem = num%10
    if rem in [2,3,7,8]:
        return False
    trem = num%100
    if trem in [26, 46, 66, 86]:
        return False
    if not rem == 6:
        temp = num
        temp /= 10
        rtemp = temp % 10
        if rtemp in [1,3,5,7,9]:
           return False
    if rem == 5:
        temp = num
        temp /= 10
        rtemp = temp % 10
        if not rtemp == 2:
            return False
    if not (trem % 4) == 0 and (rem % 2) == 0:
        return False
    return checkAgain(num)

def checkAgain(num):
    epsilon = 1e-20
    from math import sqrt
    temp = sqrt(num)
    tada = temp - round(sqrt(num))
    if abs(tada) < epsilon:
        return True
    else :
        return False


def generateCoin(N,J):
    coins = []
    pons = []
    maximum = pow(10,N)
    i = pow(10,N-1)+1

    iter = toTen(i)
    while (len(coins) < J):
        iter+=2
        tempC = toTwo(iter)
        if test(tempC):
            res = ditto(tempC)
            for ib in res:
                if not None in res:
                    coins.append(tempC)
                    pons.append(res)
                    break
    return (coins,pons)

def toTwo(n):
    temp = n
    result = 0
    i = 0
    while not (temp == 0):
        rem = temp % 2
        result += rem * pow(10,i)
        temp /= 2
        i += 1
    return result

def toTen(n):
    temp = n
    result = 0
    i = 0
    while not (temp == 0):
        rem = temp % 10
        result += rem * pow(2,i)
        temp /= 10
        i +=1
    return result

def test(coin):
    diffbases = convert(coin)
    for n in diffbases:
        if isPrime(n):
            return False
    return True
            
        

def isPrime(num):
    return pow(2, num-1,num) == 1

        

        
    
def convert(n):
    result = []
    for base in range(2,11):
        temp = n
        tempresult = 0
        i = 0
        while not (temp == 0):
            rem = temp % 10
            tempresult += rem * pow(base,i)
            temp/=10
            i+=1
        result.append(tempresult)
    return result


if __name__ == "__main__":
    main()
