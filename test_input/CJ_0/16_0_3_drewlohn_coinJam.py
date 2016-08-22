import csv as csv

print 'Starting'

inFile = open('B-small-attempt0.in','rb')
data = csv.reader(inFile,delimiter=' ')
numTests = int(data.next()[0])

outFile = open('outputSubmission.csv','wb')
outer = csv.writer(outFile)
outString = 'Case #1:' 
outer.writerow([outString])


#primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61...]

def findDivisor(testString, base):
    a = [int((base**place)*float(testString[-place-1])) for place in xrange(len(testString))]
    b = int(sum(a))
    for divisor in xrange(100000):
        divisor += 2
        if divisor > b/2:
            break
        if b%divisor==0:
            return divisor
    return 'none'


count = 0
for i in xrange(16384):
    binConv = bin(i)[2::]
    while len(binConv) < 14:
        binConv = '0'+binConv
    testString = '1' + binConv + '1'
    #print testString

    divisors = []
    for j in xrange(9):
        divisor = findDivisor(testString, j+2)
        if divisor == 'none':
            break
        else:
            divisors.append(divisor)
    if len(divisors) == 9:
        outString = testString + ' ' + ' '.join(map(str,divisors))
        print outString
        outer.writerow([outString])
        count += 1
    if count == 50:
        break

inFile.close()
outFile.close()
            
        

print 'Done'
