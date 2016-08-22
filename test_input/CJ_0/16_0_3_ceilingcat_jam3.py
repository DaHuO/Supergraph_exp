import functools
import math
import sys
import time
from decimal import *

def contains( ara, number ):
  for k in ara:
    if k == number:
      return 1
  return 0

def dumbprimetest( maybe, bases):
  start = time.time()
  #print('dpt', maybe, bases)
  for k in range(2,1+maybe//2):
    if not maybe%k and not k in bases:
      #print( maybe, k )
      return k
    if time.time() - start > 1:
      return 0
  return 0

def changebase( jamcoin, base ):
  if base == 2:
    return jamcoin
  coinstr = ''
  for k in range(32):
    if jamcoin%2:
      coinstr = '1' + coinstr
    else:
      coinstr = '0' + coinstr
    jamcoin = jamcoin >> 1
  return int(coinstr,base )

def printstuff( J, mynum, mylist ):
  tempstr = ''
  for k in range(J ):
    tempstr += '1' if (mynum>>k)%2 == 1 else '0'

  tempstr = tempstr[::-1]

  for k in range(9):
    tempstr += ' ' + str(mylist[k] )
  print( tempstr )

s=sys.stdin.read().split('\n')

ss=s[1].split()
N=int(ss[1])
J=int(ss[0])

#print( N, J )

start = 1 + ( 1<<(J-1) )
count = 0
divisors = set()

print( 'Case #1:' )

while count != N:
  bases = []
  for l in range(2,10+1):
    temp = dumbprimetest( changebase( start, l ), divisors | set(bases))
    if temp != 0:
      bases.append( temp )
    else:
      break

  #print( 'foo ', start, bases )
  if len( bases) == 9: 
    #print( start, bases )
    printstuff( J, start, bases )
    #print( len(divisors) )
    count += 1
    divisors |= set(bases)
  start += 2

quit()

print( 'Case #' + str(k+1) + ': ' + str(sum/2+1) )
