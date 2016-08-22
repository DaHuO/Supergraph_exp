#!/usr/bin/env python
"""Google Code Jam 2016: Problem B. Revenge of the Pancakes"""

from builtins import input
from itertools import groupby


def main():
  T = int(input())
  if T < 1 or T > 100:
    raise RuntimeError("T is not within the valid range")
  for i in range(T):
     S = input()
     if len(S) < 1 or len(S) > 100:
       raise RuntimeError("S is not within the valid range")
     r = flipPancakes(S)
     print("Case #" + str(i + 1) + ": " + r)
    


def flipPancakes(S):
  r = ''.join(ch for ch, _ in groupby(S))
  if r.endswith("+"):
    return str(len(r) - 1)
  return str(len(r))
  

if __name__=="__main__":
  main()
