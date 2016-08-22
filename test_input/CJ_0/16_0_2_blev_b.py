
import math
from sys import stdin
def readline(): return stdin.readline().strip('\n')
def readint(): return int(readline())
def readlineints(): return [int(x) for x in readline().split(' ')]

def minflips(p):
   flips = 0
   minus = 0
   while minus < len(p):
      hadplus = False
      while minus < len(p) and p[minus] == '+':
         hadplus = True
         minus += 1 
      if minus >= len(p): break
      while minus+1 < len(p) and p[minus+1] == '-': minus += 1
      if minus >= len(p): break
      flips += 1
      if hadplus: flips += 1
      minus += 1
   return flips

def main():
   T = readint()
   for t in range(1, T+1):
      p = readline()
      print 'Case #' + str(t) + ': ' + str(minflips(p))
 
main()
