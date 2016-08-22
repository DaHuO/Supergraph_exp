#Bill Zhang
#Coin Jam
#Google Code Jam

from math import sqrt
from random import randint

def readFile():
    file = open('C-large.in', 'r')
    #file = open('coinjamsample.txt', 'r')
    fileout = open('coinjamout.txt', 'w')
    num = int(file.readline())
    for n in range(num):
        data = file.readline().split(" ")
        N = int(data[0])
        J = int(data[1])
        fileout.write("Case #"+str(n+1)+":\n")
        vals = generateJam(N, J)
        for k in range(J):
            strFactors = [str(v) for v in vals[k][1]]
            if k != J-1:            
                fileout.write(vals[k][0]+" "+" ".join(strFactors)+"\n")
            else:
                fileout.write(vals[k][0]+" "+" ".join(strFactors))

def generateJam(N, J):
    nGen = 0
    valid = []
    while(nGen < J):
        n = bin(randint(0, 2**(N-2)-1))[2:]
        if len(n) < N-2:
            for k in range(N-2-len(n)):
                n = "0"+n
        n = "1"+n+"1"
        jt = jamTest(n)
        if len(jt[1]) > 0:
            nGen += 1
            valid.append(jt)
    return valid
    
def jamTest(num):
    hasprime = False
    b = 2
    factors = []
    while not(hasprime) and 2<=b<=10:
        x = int(num, b)
        pt = primeTest(x)
        hasprime = pt[0]
        if hasprime == True:
            return b, []
        factors.append(pt[1])
        b += 1
    if b < 11:
        factors.clear()
    elif b == 11:
        return num, factors
        
def primeTest(n):
    isprime = True
    i = 2
    while isprime and i <= sqrt(n) and i <= 200:
        if n%i == 0:
            isprime = False
        i += 1
    return isprime, i-1

readFile()