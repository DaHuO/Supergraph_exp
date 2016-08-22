def getFactor(val):
    for i in range(2, int(val**0.5)+1):
        if(val % i == 0):
            return i
    return False


def total(n):
    j = 0
    for i in range(0, n):
        j += 2**i
    return j

def printJamCoin(n, j):
    minCase = 2**(n-1) + 1
    maxCase = total(n);
    coinCount = 0
    #print(minCase, maxCase)

    for i in range(minCase, maxCase+1):
        coin = str(bin(i))[2:]
        valid = True
        totalFactors = []

        if(coin[-1] == "1"):
            #print("\nCOIN: ", coin)
            for base in range(2, 11):
                testing = int(coin, base)
                factor = getFactor(testing)
                totalFactors.append(factor)
                #print("{} testing: {}, factor: {}".format(base,testing, factor))

                if(not factor):
                    valid = False
                    break

            if(valid):
                print("{} {}".format(coin, str(totalFactors)[1:-1].replace(",", "")))
                coinCount+=1
                if(coinCount >= j):
                    #continue
                    break

def main():
    tests = int(input(""))

    for i in range(0, tests):
        line = input()
        line = line.split()
        n = int(line[0])
        j = int(line[1])
        #print(n, j)
        print("Case #{}:".format(i+1))

        printJamCoin(n, j)

main()
