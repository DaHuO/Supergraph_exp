import numpy as np
from decimal import Decimal

def generatePrimes(n):
    unprimes = []
    primes = []
    for i in xrange(2, n+1):
        if i not in unprimes:
            primes.append(i)
            for j in xrange(i**2, n+1, i):
                unprimes.append(j)
                
    return primes

prime_list = generatePrimes(10000)

def findFactor(num):
    for prime in prime_list:
        if (num % prime) == 0:
            return prime
    return 0
    

def output(i, out):
    with open('C-large.out', 'w') as outfile:
        outfile.write("Case #{0}:\n".format(i))
        for line in out:
            outfile.write("{0} {1}\n".format(line[0], ' '.join([str(x) for x in line[1]])))
        
def interpret(barray, base):
    multarr = np.power(base*np.ones(len(barray), dtype=Decimal), np.array(range(len(barray)), dtype=Decimal)[::-1])
    val = np.sum(barray*multarr)
    
    return val

def determine(num, counter, results):
    factors = []
    for rnum in range(2,11):
        val = interpret(np.array([int(x) for x in bin(num)[2:]]), rnum)
        factor = findFactor(val)
        if factor != 0:
            factors.append(factor)
        else:
            break
    if len(factors) < 9:
        pass
    else:
        counter += 1
        results.append((bin(num)[2:], factors))
        print counter    
    return counter

def solve(i, line):
    sline = line.split(' ')
    minnum = 2**(int(sline[0])-1)+1
    maxnum = 2**int(sline[0])
    
    num = minnum
    
    counter = 0
    results = []
    while (counter < int(sline[1])) and num < maxnum:
        counter = determine(num, counter, results)

        num += 2
        if num-1 % 1000 == 0:
            print num
        continue
    output(i, results)
            
    

lines = open('C-large.in').readlines()

interpret(np.array([int(x) for x in bin(4)[2:]]), 2)
for i, line in enumerate(lines):
    if i > 0:
        solve(i, line)