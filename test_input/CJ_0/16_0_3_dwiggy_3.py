#!/usr/bin/python
import sys

def perms(n, i, J, prev):
    global halfnum
    if (i == n):
        halfnum.append(prev+'0')
        halfnum.append(prev+'1')
    else:
        perms(n, i+1, J, prev+'0')
        perms(n, i+1, J, prev+'1')


Nl = int(sys.stdin.readline())

for i in range(0,Nl):
    line = sys.stdin.readline().rstrip().split(' ')
    N = int(line[0])
    J = int(line[1])
    print ('Case #'+str(i+1)+':')
    
    n = int(N//2) - 2
    
    global halfnum
    halfnum = []
    perms(n, 1, J, '')
    
    j = 0
    for num in halfnum:
        if num.strip('0') != '':
            j += 1
            num = '1'+num+'1'
            revnum = num
            if ((len(num) + len(revnum)) < N):
                revnum = '0'+revnum
            print (num+revnum, end='')
            for Z in range(2,11):
                e = N-1
                k = 0
                divisor = 0
                for c in num:
                    if (c == '1'):
                        k = e    
                    e -= 1
                divisor = (Z**k + 1)
                print (' '+str(divisor), end='')
                #print (' '+str(int((num+revnum), Z)/divisor), end='')
            print ()

        if (j == J):
            break
