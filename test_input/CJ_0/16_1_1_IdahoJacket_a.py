import sys

numCases = input()
for case in range( 1, numCases + 1 ):
  s = raw_input()
  last = s[0]
  s = s[1:]
  for c in s:
    if c < last[0]:
      last += c
    else:
      last = c + last
    s = s[1:]

  output = last

  print 'Case #' + str( case ) + ': ' + str( output )
