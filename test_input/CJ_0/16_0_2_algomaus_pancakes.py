#! /usr/bin/env python

def parse(lines):
  n = int(lines[0])
  cakes = []
  for i in range(n):
    cake = []
    for i in lines[i+1]:
      cake.append(i)
    cakes.append(cake)
  return cakes
  
def solve(cake):
  num = 0
  
  while len(cake) > 0:
    #remove the lowest 1s
    newcake = cake
    for i in reversed(range(len(cake))):
      if cake[i] == '+':
        newcake = newcake[:-1]
      else:
        break
    cake = newcake
    if len(cake) == 0:
      return num
    if cake[0] == '-':
      for i in range(len(cake)):
        # flip and invert
        if cake[i] == '+':
          cake[i] = '-'
        else:
          cake[i] = '+'
      cake[:] = reversed(cake[:])
      num = num + 1
    else:
      # turn ones into zeroes
      for i in range(len(cake)):
        if cake[i] == '+':
          cake[i] = '-'
        else:
          break
      num = num + 1
  return num
    
with open('B-large.in', 'r') as f:
#with open('input', 'r') as f:
  cakes = parse(f.read().splitlines())
for i in range(len(cakes)):
  sol = solve(cakes[i])
  print "Case #" + str(i+1) + ": " + str(sol)
