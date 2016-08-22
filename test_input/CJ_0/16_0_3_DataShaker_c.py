from collections import deque
import math

def any_divisor(n):
    for i in xrange(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return i
            if i*i != n:
                return i
    return 0


input = open('./C.in', 'r').readlines()
output = open('./C.out', 'w')

inputQueue = deque(input)
testCases = int(inputQueue.popleft())
for i in range(1, testCases+1):
    case = str(inputQueue.popleft()).split(" ",1)
    n =  int(case[0])
    j = int(case[1])
    i = int(math.pow(10,n-1) + 1)
    out = ""
    count = 0
    while True:
        #create list for bases (base 10)
        numbs = [int(str(i), base) for base in range(2, 11)]
        #primcheck
        divisors = []
        for numb in numbs:
            div = any_divisor(numb)
            if div == 0:
                break
            divisors.append(div)
        if len(divisors) == len(numbs):
            out += str(i)+" "+" ".join(str(div) for div in divisors)+"\n"
            count += 1
            if count == j:
                break
        # inc number
        i = int(bin(numbs[0]+2).lstrip('0b'))
    output.write("Case #"+str(1)+":\n"+out+"\n")
output.close()


