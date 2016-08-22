def flip(s):
   return list(reversed([-1*i for i in s]))

def movement(s,i):
    s1=s[:i+1]
    s2=s[i+1:]
    return flip(s1)+s2


def readS(s):
   out = []
   for c in s:
       if c=='+':
           out.append(1)
       elif c=="-": out.append(-1)
       
   return out

def writeS(s):
   def sign(c):
     if c==1: return '+'
     else: return '-'
   return [sign(i) for i in s]

def isSolved(s):
    return s==[1]*len(s)

def algo(s):
    times = 0
    while True:
        #print times, writeS(s)
        if isSolved(s): return times

        if s[0]==1:
           i = s.index(-1)
           s = movement(s,i-1)

        elif s[0]==-1:
           i =  len(s)-list(reversed(s)).index(-1)-1
           s = movement(s,i)


        times+=1

import sys
n = int(sys.stdin.readline())
for i in range(n):
    print "Case #%i:"%(i+1), algo(readS(sys.stdin.readline()))
        
