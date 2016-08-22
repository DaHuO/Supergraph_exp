def fromDigits(digits, b):
    n = 0
    for d in digits:
        n = int(b) * n + int(d)
    if isPrime(n) is False:
        return n
    else:
        return "Z"
def isPrime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True
def convDigits(digits, b):
    n = 0
    for d in digits:
        n = int(b) * n + int(d)
    return n
def findPrime(x):
    for i in range(2, x):
        if x % i == 0:
           return i
    return False
def toBin(x):
    return int(bin(x)[2:])
T=int(input())
N, J = map(int,input().split(" "))
S="0"*(N-2)
number="1"+S+"1"
newNum=number
print("Case #1:")
count=0
for loop in range(200):
    interpret=[]
    divisors=[]
    newNum=str(newNum)
    for i in range(2,11):
        numToConv=[int(z) for z in newNum]
        if fromDigits(numToConv,i) == "Z" or len(interpret)==9:
            break
        else:
            interpret.append(fromDigits(numToConv,i))
    if len(interpret)>=9:
        for var in range(0,len(interpret)):
            if findPrime(interpret[var]) is False:
                break
            else:
                divisors.append(findPrime(interpret[var]))
        if len(divisors)==9:
            print(newNum,end=" ")
            for var in range(0,len(divisors)):
                print(divisors[var],end=" ")
            print("")
            count=count+1
    temp=convDigits(newNum,2)
    temp=str(toBin(temp+1))
    if temp[-1] == '1':
        newNum = temp
    else:
        temp=convDigits(temp,2)
        temp=str(toBin(temp+1))
        if temp[-1] == '1':
            newNum = temp
    if len(newNum)>N:
        break
    if count==J:
        break