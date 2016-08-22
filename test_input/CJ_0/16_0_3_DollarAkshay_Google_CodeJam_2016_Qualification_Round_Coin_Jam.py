
import math

n = 32
j = 500

coin = ''
coin+='1'

for i in range(n-2):
    coin+='0'
coin+='1'

temp = []
jamcoins = []
factors = []

def isPrime(n):
    lim = math.floor(pow(n, 0.5))
    for i in range(2,lim+1):
        if n%i==0:
            temp.append(i)
            return False
    return True

def isJamCoin(c):
    global temp
    for b in range(2,11):
        if isPrime(int(c,b)):
            temp = []
            return False
    factors.append(temp)
    temp = []
    return True

print("Case #1:")
while len(jamcoins)<j:
    if isJamCoin(coin):
        jamcoins.append(coin)
        print(coin, end=" ")
        for i in range(9):
            print( factors[len(factors)-1][i], end=" ")
        print("")
    coin = bin(int(coin, 2) + 2)[2:]
    
        
    

