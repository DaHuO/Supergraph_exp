import sys
from decimal import *

s=sys.stdin.read().split('\n')

for k in range(int(s[0])):
  teststring = s[k+1]

  sys.stdout.write( 'Case #' + str(k+1) + ': ' )

  outstr = teststring[0]
  for l in range(1,len(teststring)):
    if ord(teststring[l]) >= ord( outstr[0] ):
      outstr = teststring[l] + outstr
    else:
      outstr = outstr + teststring[l]
    #print( teststring[l] + outstr[0] )
  print( outstr )
