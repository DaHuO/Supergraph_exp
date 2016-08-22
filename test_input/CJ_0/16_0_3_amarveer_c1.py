import sys
from math import sqrt
from time import time

T = time()

t = int(sys.stdin.readline())

N,J = map(int,sys.stdin.readline().split())

nums = set()

def nextbin(s):
    nextNum = bin(int(s,2)+1)[2:]
    if len(nextNum) > len(s):
        print "Length exceeded"
    return '0'*(len(s)-len(nextNum)) + nextNum

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False    
    return True

def factor(n):
    if n % 2 == 0:  return 2
    for i in xrange(3,n+1,2):
        if n%i == 0:    return i

def factor1(n):
    if n % 2 == 0:  return 2
    t = 3
    while t < 10**5 and t < n:
        if n%t == 0:    return t
        t += 2
    return -1

num = 2147483649

print "Case #1:"

while len(nums) != J:
    num = bin(num)[2:]
    ans = num
    flag = True
    for i in xrange(2,11):
        f = factor1(int(num,i))
        if f == -1:
            flag = False
            break
        ans += " %d"%(f)
    if flag:
        nums.add(ans)
        print ans
    num = int(num,2) + 2



