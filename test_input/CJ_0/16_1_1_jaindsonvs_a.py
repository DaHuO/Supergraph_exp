#!/usr/bin/env python
# -*- coding:utf-8 -*-

def readint(): return int(input())
def readfloat(): return float(input())
def readarray(N, foo):
        res = []
        for _ in xrange(N):
                res.append(foo())
        return res
def readlinearray(foo): return map(foo, input().split())

def better_left(ans, l):
  return ans[0] <= l

def solve(S):
  ans = ''
  for l in S:
    if ans == '':
      ans += l
    else:
      ans = l + ans if better_left(ans, l) else ans + l
  return ans
  
if __name__ == '__main__':
  T = readint()
  for t in range(1, T+1):
    S = input()
    ans = solve(S)
    print('Case #%d: %s' % (t, ans))