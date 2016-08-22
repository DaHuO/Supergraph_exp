import random, math, re

def isPrime(numCheck):
    '''
    returns True if number is prime, false if not
    '''
    if numCheck==2 or numCheck==3: 
        return True
    if numCheck%2==0 or numCheck<2: 
        return False
    for i in range(3,int(numCheck**0.5)+1,2):   # only odd numbers
        if numCheck%i==0:
            return False    

    return True    
    

def isPrimeBases(numCheck):
    '''
    return True if number is prime in at least one base 2 through 10 inclusive
    
    will return False if prime not prime in any
    '''
    
    primeFound = True
    
    for i in range(2,11):
        primeFound = isPrime(int(str(numCheck), i))
        
        if primeFound == True:
             break 
        
    return primeFound
    
        
    
def findDivisorsBase(numCheck):
    '''
    return all nontrivial divisors for all 10 bases
    '''
    
    divisors = []
    
    for b in range(2,11):
        basenumCheck = int(str(numCheck),b)
        for i in xrange(2, int(math.sqrt(basenumCheck) + 1)):
            if basenumCheck % i == 0:
                divisors.append(i)
                break
            #if i*i != n:
            #    large_divisors.append(n / i)
      
    return divisors

def checkDigits(numCheck):
    '''
    checks to make sure the first and last digit is 1
    
    returns True/False
    '''
    
    stringNum = str(numCheck)
    
    return bool(int(stringNum[0]) and int(stringNum[len(stringNum)-1]))
    
def generateNumber(length):
    '''
    returns a string of length length of 1s and 0s
    '''
    number = ''
    
    for j in range(length):
        if j == 0 or j == length-1:
            number += "1"
        elif random.random()<.5:
            number += "1"
        else:
            number +="0"
    
    return number
    
## OPENING FILE TO SEE HOW LONG COINS ARE AND HOW MANY

inputfile = open("coins.txt")

lines = []

for line in inputfile:
    lines.append(line)

inputfile.close() 

nfind = re.search('(\d*) (\d*)', lines[1])
N = int(nfind.groups()[0])
J = int(nfind.groups()[1])

    
## BEGINNING            
jamcoins = {}

while len(jamcoins) < J:
    newNumber = generateNumber(N)
    if not isPrimeBases(int(newNumber)): # if the new number isn't prime in any base, check to see if already found
        if newNumber not in jamcoins.keys():
            divisors = findDivisorsBase(newNumber)    
            jamcoins[newNumber] = divisors #replace with list of divisors
        

newfile = open("jamcoins.txt",'w')       

newfile.write("Case #1:" +'\n')
for jc in jamcoins:
    newfile.write(jc + ' ')
    for d in jamcoins[jc]:
        newfile.write(str(d) + ' ')
    newfile.write('\n')
    
newfile.close()           