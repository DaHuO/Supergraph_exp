#!/usr/bin/env python3

import sys
from collections import deque

def last_word(word):
  l = list(word)
  o = deque()
  o.append(l[0])

  for c in l[1:]:
    if c < o[0]:
      o.append(c)
    else:
      o.appendleft(c)

  return "".join(o)

file  = open(sys.argv[1])
total = int(file.readline())

for i in range(1, total + 1):
  word   = file.readline().rstrip()
  result = last_word(word)
  print("Case #%d: %s" % (i, result))