def findFactor(n):
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            return i
        i += 1
    return 0

jamcoins = []
currInt = 2**15+1
print currInt

while len(jamcoins) < 50 and currInt < 2**16:
    binStr = str(bin(currInt))[2:]
    composites = []
    for i in range(2,11):
        num = int(binStr, i)
        x = findFactor(num)
        if x:
            composites += [x]
    if len(composites) == 9:
        jamcoins += [composites]
        print len(jamcoins)
        outputF = open('jamcoins_16.txt', 'a')
        outputF.write(binStr + ' ')
        for j in composites:
            outputF.write(str(j) + ' ')
        outputF.write('\n')
        outputF.close()
    currInt += 2


    


