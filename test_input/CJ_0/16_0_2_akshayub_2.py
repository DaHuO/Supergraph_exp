import sys
import math

test = input()
pancake = []
flip = 0
x = 0
y = 0

for x in xrange(test):
    a = raw_input()
    pancake.append(a)

for x in xrange(test):
    
    flip = 0
    a =[]
    pan = list(pancake[x])

    while(1):

        if '-'*len(pancake[x]) == pancake[x]:
            pancake[x] = '+'*len(pancake[x])
            flip += 1

        if '+'*len(pancake[x]) == pancake[x]:
            break

        for y in xrange(len(pancake[x])-1):
            
            if pan[y] != pan[y+1]:
                break
            
        a = pan[:y+1]
        pan = pan[y+1:]

        for i in range(y+1):
            if a[i] == '+':
                a[i] = '-'
            else:
                a[i] = '+'

        flip += 1

        pan = a + pan

        pancake[x] = ''.join(pan)
        
    print 'Case #%d:' %(x+1) , flip
