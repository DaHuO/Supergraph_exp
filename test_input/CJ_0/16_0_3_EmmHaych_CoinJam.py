def main():
    raw_input()
    N, J = map(int, raw_input().split())
    middleNumber = 0
    divisors = []
    
    print "Case #1:"

    while (J != 0):
        divisors = []
        error = 0
        middleNumberBin = bin(middleNumber)[2:].zfill(N - 2)
        if(len(middleNumberBin) > N - 2):
            print 'middle num exceeded'
            break
        jamcoin = '1' + middleNumberBin + '1'
        
        for currentBase in range(2, 11):
            ones = getOnes(jamcoin)
            result = 0
            for currentOne in ones:
                result = result + pow(currentBase, currentOne)
            divisor = getDivisor(result)
            if(divisor == result):
                error = 1
                break
            if(divisor == -1):
                error = 1
                break
            divisors.append(getDivisor(result))
        
        middleNumber = middleNumber + 1
        
        if(error == 1): continue
        else:
            finalResult = jamcoin
            for currentDivisor in divisors:
                finalResult = finalResult + ' ' + str(currentDivisor) 
            print finalResult
            J = J - 1

def getOnes(string):
    result = []
    i = len(string) - 1
    for char in string:
        if char == '1':
            result.append(i)
        i = i - 1
    return result

def getDivisor(number):
    divisor = 2
    while True:
        if(number % divisor == 0): return divisor
        if(divisor > pow(10, 2)): return -1
        divisor = divisor + 1
        
main()