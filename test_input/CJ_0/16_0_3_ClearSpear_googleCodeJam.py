"""
def numberOfTimes(case):
    seen_letters = []
    for i in list(str(case)):
        if i not in seen_letters:
            seen_letters.append(i)
    n = 1
    number = n * case
    while len(seen_letters) < 10:
        number = n*case
        n+=1
        for i in list(str(number)):
            if i not in seen_letters:
                seen_letters.append(i)
        if n > 1000:
            return "INSOMNIA"
    return number
"""

"""
def trimRight(order):
    if order == "+":
        return ""
    if order[len(order) - 1] == "+":
        return trimRight(order[:-1])
    else:
        return order 

def flip(order):
    flippedOrder = ""
    for i in order:
        if i == "+":
            flippedOrder = flippedOrder + "-"
        if i == "-":
            flippedOrder += "+"
    return flippedOrder

def pancakeFlips(order):
    flips = 0
    while len(order) > 0:
        order = trimRight(order)
        order = flip(order)
        flips += 1
    return flips - 1 
"""

import math 

def nonTrivialDivisor(number):
    for i in range(2, int(math.floor(math.sqrt(number))) + 1):
        if number%i == 0:
            return i
    return "prime"

def isJamCoin(coin): 
    coin_letters = list(str(coin))
    for i in coin_letters:
        if i != "0" and i != "1":
            #print "invalid digit"
            return False 
    if coin_letters[0] != "1" or coin_letters[len(coin_letters)-1] != "1":
        #print "bad endpoints"
        return False 
    proof = []
    for b in range(2,11):
        convertedInt = int(str(coin), b)
        factor = nonTrivialDivisor(convertedInt)
        if factor == "prime":
            return False 
        proof.append(factor)
    return proof

#print(isJamCoin(111001))

def findJamCoins(length, number):
    found = 0
    test = 10**(length-1)
    jamCoins = []
    proofs = []
    while found < number and test < 10**(length):
        factors = isJamCoin(test)
        if factors != False :
            jamCoins.append(test)
            proofs.append(factors) 
            found += 1
        test+=1
    return [jamCoins,proofs]

#print(findJamCoins(6, 3))

dataFile = open("googleCodeJamTestFile.in")
data = []
for i in dataFile:
    data.append([int(j) for j in i.split()])
#print data

answer = open("googleCodeJamDumpFile.in", 'w')
answer.write("Case #1:\n")

print("Finding Solution...")
solution = findJamCoins(data[1][0], data[1][1])
print("Found solution!")

jamCoins = solution[0]
proofs = solution[1]

print jamCoins
print proofs

for i in range(0,len(jamCoins)): 
    answer.write(str(jamCoins[i]) + " ")
    for j in range(0, len(proofs[i])):
        answer.write(str(proofs[i][j]))
        if (j < len(proofs[i]) - 1):
            answer.write(" ")
    if( i < len(jamCoins) - 1):
        answer.write("\n")
