#!/usr/bin/python
import sys
def raw_input(f=open(sys.argv[1])): return f.readline().rstrip()
t = int(raw_input())
for i in range(t):
   o = ''
   s = raw_input()
   for c in s:
      if not len(o) or c >= o[0]:
         o = c + o
      else:
         o += c
   print 'Case #%d: %s' % (i+1, o)

