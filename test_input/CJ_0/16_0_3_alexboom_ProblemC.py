'''
Created on 9 Apr 2016

@author: boom
'''
import random
import threading

class JamcoinGenerator():
    
    def __init__(self, length, number):
        self.length = length
        self.number = number
        
    def jamcoin(self):
        
        int_range = range(2**(self.length-1)+1, 2**self.length, 2)
        numberBuff = [int('{0:0b}'.format(x)) for x in int_range]
        
        t1 = threading.Thread(target=self.parallels(self.number/2, numberBuff[:len(numberBuff)/2]))
        t2 = threading.Thread(target=self.parallels(self.number/2, numberBuff[-(len(numberBuff)/2):]))
        
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()
        
        
    def parallels(self, number, numberBuff):
        
        nonprimes = self.filter(numberBuff)
        output = list()
#         return nonprimes

        indexes = range(0, number)
        random.shuffle(indexes)
        for i in indexes:
            jam = nonprimes[i]
            factors = list()
            factors.append(jam)
            for base in range(2, 11):
                converted = int(str(jam), base)
                factors.append(self.getFactor(converted))
            
            output.append(factors)
        for sets in output:
            print ' '.join(map(str, sets))
        
    def filter(self, array):
        
        filtered = list()
        for i in array:
            checks = 0
            for base in range(2, 11):
                converted = int(str(i), base)
#                 print 'PRIME'
                if self.checkPrime(converted): break
                else: checks = checks + 1
            if checks == 9: filtered.append(i)
     
        return filtered
    
    def getFactor(self, number):
        factorSpace = range(2, int(number**0.5) + 1)
        random.shuffle(factorSpace)
        for i in factorSpace:
            if number%i == 0: return number//i
        return 0
    
    def checkPrime(self, n):
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
    
def main():
    
    testFile = 'problemC.txt'
    with open(testFile) as f:
        lineCount = 1
        next(f)
        for line in f:
            currLine = line.rstrip('\n')
            lenght, number = currLine.split()
            generator = JamcoinGenerator(int(lenght), int(number))
            print 'Case #' + str(lineCount) + ':'
            generator.jamcoin()
#             for output in generator.jamcoin():
            lineCount = lineCount + 1
            if lineCount > 100 : break

if __name__ == '__main__':
    main()