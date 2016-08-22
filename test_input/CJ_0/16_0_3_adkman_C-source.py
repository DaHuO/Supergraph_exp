import re
import itertools

def isPrime(n):
    if n == 2:
        return 0
    if n == 3:
        return 0
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return i
        i += w
        w = 6 - w
    return 0

def genStrings(n):
    return ["".join(seq) for seq in itertools.product("01", repeat=n)]

t = input()
print("Case #"+t+":")
string = input()
string = string.strip().split(" ")
n = int(string[0])
j = int(string[1])

tempBitString = genStrings(n)
for s in range(32769, 65536):
    if not (s&1):
        continue
    string = tempBitString[s]
    bitString = []
    for x in range(2, 11):
        temp = isPrime(int(str(string), x))
        if temp:
            bitString.append(temp)
        else:
            break
    if len(bitString)!=9:
        continue
    else:
        j = j-1
        print(string, end=" ")
        for b in bitString:
            print(b, end=" ")
        print("")
        if not j:
            break