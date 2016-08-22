import sys 
import math

T = int(sys.stdin.readline())

for case in range(T):
  pancakes = sys.stdin.readline().strip()

  # trim +s from the end
  pancakes = pancakes.rstrip('+')

  if len(pancakes) == 0:
    print "Case #%i: 0" % (case+1)
    continue

  # count the number of inflections
  last_side = pancakes[0]
  steps = 1
  for pancake in pancakes:
    if pancake != last_side:
      steps = steps + 1
      last_side = pancake

  print "Case #%i: %s" % (case+1, steps)

