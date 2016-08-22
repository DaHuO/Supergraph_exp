import math
readFile = open("C-large.in")
testCases = eval(readFile.readline())
N,J = map(int, readFile.readline().split())
ans = {}
def calBaseValue(base2Value,base):
    binary = bin(base2Value)
    binary = binary[2:]
    baseValue = 0
    power = 0
    for i in range(len(binary)-1,-1,-1):
       baseValue += int(binary[i])*(base**power)
       power += 1
    return baseValue

def removePrimeNum(jamCoinsArr):
    tempArr = []
    for i in range(0,len(jamCoinsArr)):
      num = jamCoinsArr[i]
      for j in range(2,500):
        if(num%j==0):
          tempArr.append(str(num/j))
          break
    return tempArr  
     
def findBase2JamCoins(a,b,jamCoinsArr):
    for i in xrange(a,b):
       if (i%2) == 1:
          jamCoinsArr.append(i)

#find all prime numbers between 1000000000000001 and 1111111111111111 for all bases
jamCoinsArr = []
base2min = '1'+(N-2)*'0'+'1'
minBase = int(base2min,2)
maxBase = minBase+20000;

#find all base2 which start and end with 1 and not prime
findBase2JamCoins(minBase,maxBase,jamCoinsArr)
#Remove primeNumbers from jamCoinsArr
count = 0
for i in range(0,len(jamCoinsArr)):
    tempArr = []
    ansArr = ''
    tempArr.append(jamCoinsArr[i])
    for base in range(3,11):
        tempArr.append(calBaseValue(jamCoinsArr[i],base))
    arr = removePrimeNum(tempArr)
    if len(arr) == 9:
       binary = bin(jamCoinsArr[i])
       ansArr = binary[2:]+' '+' '.join(arr)
       ans[count] = ansArr
       count += 1
    if count == J:
       break

outputFile = open("Coin_Jam_output.txt",'w')
outputFile.write("Case #1: \n")
for i in range(0,len(ans)):
    outputFile.write(ans[i]+"\n")
