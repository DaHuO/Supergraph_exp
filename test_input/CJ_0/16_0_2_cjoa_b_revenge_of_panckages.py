#!/usr/bin/env python

from sys import stdin, stderr
import string

def solve(s):
   res = 0
   last_ch = s[0]
   for ch in s[1:]:
      if ch != last_ch:
         res += 1
      last_ch = ch
   if last_ch == '-':
      res += 1
   return res

def main():
   TC = int(stdin.readline().strip())
   for tc in xrange(1, TC+1):
      s = stdin.readline().strip()
      res = solve(s)
      print 'Case #%d: %d' % (tc, res)
   return 0

if __name__ == '__main__': main()
