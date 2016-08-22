#!/usr/bin/env python

T = int(raw_input())

visited = {}

def maneuver(l, i):
  o = []
  for ii in range(i-1, -1, -1):
    o.append(l[ii] ^ 1)
  o += l[i:]
  return o

def findSplits(s):
  o = []
  prev = s[0]
  for i in range(len(s)):
    if s[i] != prev:
      o.append(i)
      prev = s[i]
      #print 'split', s[:i]
  return o

def read_problem():
  stack = [ 1 if c=='+' else 0 for c in raw_input() ]
  return stack

def listToHash(l):
  return "-".join([str(i) for i in l])

def minMoves(level, stack):
  global visited
  splits = findSplits(stack)
  if not splits:
    # all the same
    if stack[0] == 1:
      visited[listToHash(stack)] = level
      return level
    else:
      visited[listToHash(stack)] = level + 1
      return level + 1
  res = None
  #print level*' ', stack, 'splits', splits
  for i in splits:
    stack1 = maneuver(stack, i)
    if listToHash(stack1) in visited:
      return visited[listToHash(stack1)]
    #print level*' ', 'down', stack1, level + 1
    res1 = minMoves(level + 1, stack1)
    visited[listToHash(stack1)] = res1
    if not res:
      res = res1
    else:
      res = min(res, res1)
  #visited[listToHash(stack)] = res
  return res

def solve(problem):
  global visited
  stack = problem
  #print stack, findSplits(stack)
  visited = {}
  return str(minMoves(0, stack))

for n in range(T):
  problem = read_problem()
  solution = solve(problem)
  print 'Case #%d: %s' %(n+1, solution)

