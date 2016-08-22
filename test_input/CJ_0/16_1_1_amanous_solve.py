#!/usr/bin/env python

T = int(raw_input())

def read_problem():
  s = raw_input()
  return s

def solve(problem):
  s = problem
  o = s[0]
  for c in s[1:]:
    if c >= o[0]:
      o = c + o
    else:
      o = o + c
  return o

for n in range(T):
  problem = read_problem()
  solution = solve(problem)
  print 'Case #%d: %s' %(n+1, solution)

