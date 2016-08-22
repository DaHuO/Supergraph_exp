#!/usr/bin/python
import os
from math import sqrt; from itertools import count, islice
from fractions import gcd

def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False
    return True

def divisor(n):
    for i in range(2, 1000000):
        if (n % i == 0):
            return i
               

def main():
    base = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    array = []
    i = 32769
    j = 65535
    count = 0
    print "Case #1: "
    while i < j and count < 50:
        m = 1
	for b in base:
            num = int(bin(i).replace('0b', ""), b)
            if (isPrime(num)):
                m = 0
                array = []
                break
            else:
                array.append(divisor(num)) 
        if (m != 0):
           count = count + 1
           print "%d %d %d %d %d %d %d %d %d %d" % (num, array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8])
           array = [] 
	i = i+2
          
    
if __name__ == "__main__":
    main()
