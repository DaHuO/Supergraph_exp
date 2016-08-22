#!/usr/bin/python

import  sys

def naive0(S):
  answer = ''
  for c in S:
    answer = max(c+answer, answer+c)
  return answer

line = sys.stdin.readline().strip()
nInputs = int(line)
#print >>sys.stderr, "    nInputs = "+`nInputs`
for iInput in xrange(nInputs):
  line = sys.stdin.readline().strip()
  #print >>sys.stderr, "        line = "+`line`
  S = line
  answerNaive = naive0(S)
  print "Case #%s: %s" % (iInput+1, answerNaive)

