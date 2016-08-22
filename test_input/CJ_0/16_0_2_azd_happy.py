#!/usr/bin/python
import sys
def raw_input(f=open(sys.argv[1])): return f.readline().rstrip()
n = int(raw_input())
for i in range(1, n+1):
   t = 0
   s = raw_input()
   p = s[0]
   for j in s[1:]:
      if p != j:
         t += 1
         p = j
   if s[-1] == '-':
      t += 1
   print 'Case #%d: %s' % (i, t)

