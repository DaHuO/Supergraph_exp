import sys

def flipcakes(cakes):
  prv = cakes[0]
  topstack = cakes[0]
  flips = 0
  for c in cakes[1:]:
    if c != prv:
      flips += 1
      topstack = '+' if prv == '-' else '-'
      # print('flipped, topstack now %s' % topstack)
    prv = c
  if topstack == '-':
    # print('extra final flip')
    flips += 1
  return flips

t = int(sys.stdin.readline())
for i in range(1, t + 1):
  print('Case #%d: %d' % (i, flipcakes(sys.stdin.readline().strip())))
