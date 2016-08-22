#!/usr/local/bin/python

def r():
  with open('a.in', 'r') as f:
    l = f.readlines()
    y = [x.rstrip('\n') for x in l[1:]]
    return [list(x) for x in y]
x = r()

def f(x, i):
  y = x[i:]
  z = x[:i]
  z = z[::-1]
  z = ['+' if x == '-' else '-' for x in z]
  return z + y

def s(x):
  z = x[0]

  p = True
  if z == '-':
    p = False

  y = 0
  for i, v in enumerate(x):
    if v == z:
      y = i
      continue
    break

  for v in x[y+1:]:
    if v == z:
      return False
  return True

def g(x):
  i = 0

  while True:
    while x and x[len(x) - 1] == '+':
      x = x[:len(x) - 1]
    if not x:
      return i
   
    y = len(x) - 1
    while x[0] != x[y]:
      y -= 1
    x = f(x, y + 1)
    i += 1
    
def w(a):
  with open('b.out', 'w') as f:
    for i, v in enumerate(a):
      f.write("Case #" + str(i + 1) + ': ' + str(v) + '\n')
      
a = [g(i) for i in x]
w(a)

