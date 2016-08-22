# Google Code Jam Qualification Round - Problem C
def getFiles(name):
    return open(name + '.in', 'r'), open(name + '.out', 'w')

name = 'example'
name = 'C-small'
#name = 'C-large'

# Make these global variables
N = 0
J = 0

inFile, outFile = getFiles(name)

# Returns (isPrime, oneFactor)
def isPrime(number):
    if number == 2:
        return (True, 0)
    elif number ==  3:
        return (True, 0)
    elif number % 2 == 0:
        return (False, 2)
    elif number % 3 == 0:
        return (False, 3)

    i, w = 5, 2
    while i * i <= number:
        if number % i == 0:
            return (False, i)
        i += w
        w = 6 - w
    return (True, 0)

def isJamCoin(coin):
    # Make sure the coin is long enough and has 1's on both ends
    if len(coin) < 2 or coin[0] is not '1' or coin[-1] is not '1':
        return (False, 0)

    factors = [0 for _ in range(2, 11)]

    # Check to make sure that each of the interpretations is NOT prime
    # 2 to 10 inclusive
    for i in range(2, 11):
        parsedInt = int(coin, i)
        # check if parsedInt is prime
        prime = isPrime(parsedInt)
        if prime[0] == True:
            return (False, 0)
        else:
            factors[i - 2] = prime[1]

    # Wasn't prime so it's a jam coin
    return (True, factors)

def getValue():
    global N
    # Subtract off the two ends of N
    N -= 2

    # Go through all the possibile "coins"
    def binaryGenerator(n, iter):
        global J
        if iter is 0:
            # This is a number to test
            coin = "1" + n + "1"
            jamCoin = isJamCoin(coin)
            if J > 0 and jamCoin[0] == True:
                J -= 1
                factors = jamCoin[1]
                row = coin + ' ' + ' '.join(str(e) for e in factors)
                print(str(J) + ": " + row)
                outFile.write(row + '\n')
        elif J > 0:
            binaryGenerator(n + "0", iter - 1)
            binaryGenerator(n + "1", iter - 1)

    binaryGenerator("", N)

# Number of test cases
T = int(inFile.readline())

# Read in each row
for counter in range(T):
    line = inFile.readline()
    if line != '':
        N, J = map(int, line.split())
        outFile.write("Case #" + str(counter + 1) + ":\n")
        getValue()

inFile.close()
outFile.close()
