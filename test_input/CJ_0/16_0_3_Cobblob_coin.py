import math

def bits(n, size):
    s = "{0:b}".format(n)
    while len(s) < size:
        s = "0"+s
    return s

def factor(n):
    if (n%2 == 0):
        return 2
    #for i in range(3, int(math.sqrt(n)) + 2, 2):
    for i in range(3, 1000, 2):
        if n%i == 0:
            return i
    return -1

def testJamCoin(coin):
    s = coin
    for base in range(2, 11):
        v = int(coin, base)
        f = factor(v)
        if (f == -1): # is prime
            return ""
        s += " "+str(f)
    return s


def solve(n, j):
    j, n = int(j), int(n)
    numCoinsLeft = j
    coins = ""
    for i in xrange((2)**(n-2)):
        coin = "1"+bits(i, n - 2)+"1"
        print n
        result = testJamCoin(coin)
        if (result != ""):
            numCoinsLeft -= 1
            coins += result + "\n"
            if numCoinsLeft == 0:
                break
    return coins

def main():
    f = open("input.txt", 'r')
    lines = f.readlines()
    f.close()

    outFile = open("out.txt", 'w')
    n, j = lines[1].split(' ')
    out = "Case #1:\n" + solve(n, j)
    outFile.write(str(out))


main()