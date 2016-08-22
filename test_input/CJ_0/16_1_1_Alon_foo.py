#!/usr/bin/python
import sys

def calc(S):
  lets = list(S)
  ret = [S[0]]
  for let in lets[1:]:
    if ord(let) < ord(ret[0]):
      ret.append(let)
    else:
      ret = [let]+ret
  return "".join(ret)

def main():
  d = file(sys.argv[1]).readlines()
  n = int(d[0])
  for j in xrange(1,n+1):
    S = d[j][:-1]
    print "Case #%d: %s" % (j, calc(S))

main()
