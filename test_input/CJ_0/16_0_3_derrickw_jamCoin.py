
LOWERBASE = 2
UPPERBASE = 10


def findJs(nList,J):
    jamCoinList = []

    for item in nList:
        jamCoinDivisorList = []

        for i in range(LOWERBASE,UPPERBASE+1,1):
            convertedNum = convertNum(item,i)
            #print(item, convertedNum)
            verdict, divisor = checkPrime(convertedNum)
            if verdict == False:
                jamCoinDivisorList.append(divisor)
            else:
                break
        if len(jamCoinDivisorList) == UPPERBASE - LOWERBASE + 1:
            jamCoinList.append((item, jamCoinDivisorList))

        if len(jamCoinList) == J:
            break

    return jamCoinList


def convertNum(number,base):
    newNum = 0

    for i in range(0,len(number)):#-1,-1,-1):
        newNum += int(number[i])*base**(len(number)-i-1)
    return newNum


def createNList(newStringList, newString, N):
    newStringOne = ""
    newStringZero = ""
    if N == 1:
        newString += "1"
        newStringList.append(newString)
    else:
        newStringOne += newString + "1"
        createNList(newStringList,newStringOne,N-1)
        newStringZero += newString + "0"
        createNList(newStringList,newStringZero,N-1)


def createHighestN(N):
    newN = ""
    for i in range(N):
        newN += "1"

    return int(newN)


def checkPrime(num):
    for i in range(LOWERBASE, int(num**0.5) + 1,1):
        if num % i == 0:
            return False, i
    return True, None


def main():
    t = int(input())  # read a line with a single integer
    N, J = [int(s) for s in input().split(" ")]  # read a list of integers
    print ("Case #{}:".format(1)) # {} {}".format(i, N, J))
    nList = []
    createNList(nList,"1",N-1)
    for items in findJs(nList,J):
        print (items[0], " ".join([str(item) for item in items[1]]))

if __name__=='__main__':
    main()
