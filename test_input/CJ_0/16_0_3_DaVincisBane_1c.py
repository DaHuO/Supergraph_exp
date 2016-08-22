import itertools


def generateBinary(x, j):
    binary = []
    prod = list(itertools.product("01", repeat=x))
    for numlist in prod:
        num = ""
        for n in numlist:
            num += n
        if num[0] == "1" and num[x - 1] == "1" and checkBases(num) is True:
            binary.append(num)
            ntdivs = generateNonTrivialDivisors(num)
            binary.append(ntdivs)
            currentResults = len(binary) / 2
            #print(currentResults)
            if currentResults == j:
                break
    for i in range(0, len(binary), 2):
        line = binary[i]
        for j in range(len(binary[i + 1])):
            line += " " + str(binary[i + 1][j])
        print(line)


def checkBases(x):
    #print("checkBases")
    result = True
    for base in range(2, 11):
        numberInBase = int(x, base)
        if isPrime(numberInBase) is True:
            result = False
            return result
    return result


def generateNonTrivialDivisors(x):
    #print("genNtDiv")
    ntDivisors = []
    for base in range(2, 11):
        numberInBase = int(x, base)
        ntDivisors.append(generateNTDivisor(numberInBase))
    return ntDivisors


def generateNTDivisor(numberInBase):
    #print("genSingleNT")
    for div in range(2, numberInBase):
        divres = numberInBase / div
        if divres == int(divres):
            return int(divres)


def isPrime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


with open("C-small-attempt1.in", "r") as given:
    count = 0
    maxlines = 0
    for line in given:
        count = count + 1
        if count == 1:
            maxlines = int(line)
        elif count <= maxlines + 1:
            content = line.split(" ")
            print(("Case #" + str(count - 1) + ":"))
            generateBinary(int(content[0]), int(content[1]))
            #print("done")
