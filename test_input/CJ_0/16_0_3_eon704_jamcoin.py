from math import sqrt
import math
import logging



testcases = int(input())
case = input()
n,m = map(int, case.split())



def divider(n):
    for i in range(2,math.floor(sqrt(n)+1)):
        if n%i==0:
            return i
    return -1



start = 2**(n-1)+1
finish = 2**n
count = 0
print("Case #1: ")

for i in range(start,finish):
    if count == m:
        break
    divs =[]
    number = "{0:b}".format(i)
    if number[-1] == '0':
        continue
    for j in range(2,11):
        num = int(number,j)
        d = divider(num)
        if d!=-1:
            divs.append(d)
        else:
            break

    if len(divs) == 9:
        #logging.warning(number)
        print(number, end=" ")
        for j in divs:
            print(j, end=" ")
        count += 1
        print()
