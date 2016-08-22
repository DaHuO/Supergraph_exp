import sys
from decimal import *

def expand( cakes ):
  pass

s=sys.stdin.read().split('\n')

for k in range( int(s[0]) ):
  cakes1 = s[k+1]

  cakes2 = cakes1[::-1]
  temp = cakes2.find( '-' )

  if temp == -1:
    print( 'Case #' + str(k+1) + ': 0' )
    continue
  
  cakes2 = cakes2[temp:]

  sum = 0
  for l in range(len(cakes2)-1):
    sum += abs(ord(cakes2[l])-ord(cakes2[l+1]))

  print( 'Case #' + str(k+1) + ': ' + str(sum/2+1) )
