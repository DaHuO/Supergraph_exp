
from collections import deque
from math import log

t = int(input())


def flip(string, n):
    toFlip = string[n-1::-1]
    copy = ""
    for c in toFlip:
        if c == '+':
            copy += '-'
        else:
            copy += '+'

    copy += string[n:] 
    return copy  


def allGood(string):
    return len(set(string)) == 1 and string[0] == '+'


for i in range(t):

    stack = input()
    
    if allGood(stack):
        print("Case #{0}: {1}".format(i+1, 0))
        continue

    length = len(stack)

    found = False
    row = 1
    queue = [stack]
    queue2 = []
    while(True):
        elt = queue.pop()

        for case in range(1,length+1):
            flipped = flip(elt, case)
            if allGood(flipped):
                print("Case #{0}: {1}".format(i+1, row))
                found = True
                break

            queue2.append(flipped)  

        if found:
            break

        if len(queue) == 0:
            queue = list(set(queue2))
            queue2 = []
            row += 1

        
       
        
        
        

