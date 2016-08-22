from random import *
import math
#read input file 
with open('input.txt') as input_file:
    lines = input_file.readlines()
    
txt = open("output.txt", "ab")
case = []
case = lines[1]
case = map(int, case.split(" "))
N = case[0]
J = case[1]
counter = 0;

def base_calc(number, n):
    l = len(number)
    arr = []
    for i in range(0, l):
        m = math.pow(n, l-i-1)
        arr.append(int(m))
    s = [a*b for a,b in zip(arr,number)]
    return sum(s)

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def yes(n):
    for i in range(0,9):
       if isprime(n[i]):
           return False
    return True
        

def getout(nums):
    out = ""
    for i in range(0,9): 
        n = nums[i]
        for x in xrange(2, int(math.sqrt(n) + 1)-1):
            if n % x == 0:
                if i<9 :
                    out += str(x)+" "
                else:
                    out += str(x)
                break
    return out   
    
    
        
history = []
txt.write("Case #1:\n")
n = int(math.pow(2, N)-1)
while counter != J :
    number = [] 
    for ch in str(bin(n)[2:]).zfill(N):
        number.append(int(ch))
    if number[0] == 1 and number[N-1] == 1:
        bases = []
        for i in range(0, 9):
                bases.append(base_calc(number, i+2))
        if bases[8] not in history and yes(bases):
            history.append(int(''.join(map(str, number))))
            txt.write(str(bases[8])+" "+getout(bases)+"\n")
            print str(bases[8])+" "+getout(bases)
            counter+=1
            #txt.write(out)
    n -=1

           

#txt.write(output)       
txt.close()

