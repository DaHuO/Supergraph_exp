from __future__ import print_function
import math



output = open("output3.txt", "w")

def isPrime(num):
    for i in range(2, int(math.sqrt(num) + 2)):
        if(num % i == 0):
            return i
    return -1

def convertToBase(num, base):
    ret = 0
    num = num[::-1]
    for i in range(0, len(num)):
        ret += int(num[i]) * pow(base, i)
    return ret

def nextJamCoin(length, count):
    nxt = str("{0:0{1}b}".format(count, length))
    nxt = "1" + nxt + "1"
    return nxt

print(convertToBase("100011" , 5))
print(isPrime(35))

output.write("Case #1:\n")

target = 50
size = 16
count = 0
for i in range(0, pow(2, size-2) -1):
    s = nextJamCoin(size-2, i)
    """print("JamCoin: ", s)
    print("Count: ", count)
    print("Target: ", target)
    print("convertToBase: ", convertToBase(s, 2))"""



    if target <= 0:
        break
    outputline = s + " "
    isJamCoin = True
    for j in range(2,11):
        x = isPrime(convertToBase(s, j))
        if x < 0:
            isJamCoin = False
        else:
            outputline += ( str(x) + " ")

    if isJamCoin:
        output.write(outputline.strip())
        print(outputline.strip())
        output.write("\n")
        target -= 1
