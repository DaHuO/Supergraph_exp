#!/usr/bin/python
import sys, math, re

def is_possible(field, row_max, col_max):
  for i in range(len(row_max)):
    for j in range(len(col_max)):
      v = field[i][j]
      if v < row_max[i] and v < col_max[j]:
        return False
  return True
  

T = int(sys.stdin.readline())
for t in range(T):
  s = sys.stdin.readline().strip()
  count = 0
  l = len(s) - 1
  last = s[l]
  if last == "-":
    count = 1
  else:
    # skip + at end
    while l >= 0 and s[l] == "+":
      l -= 1
    
  while l >= 0:
    c = s[l]
    if c != last:
      count += 1
      last = c
    l -= 1
  
  print("Case #%d: %d" % (t + 1, count))
