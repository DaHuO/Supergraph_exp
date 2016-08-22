#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def solve(cipher):
  flips = 0
  current_run = None
  stack = list(cipher)
  for i in xrange(0, len(stack)):
    if i == len(stack)-1:
      #print("B i = " + str(i))
      if stack[i] == "-" and (current_run != None and current_run != stack[i]):
        flips += 2
      elif current_run != None and current_run != stack[i]:
        flips += 1
      elif stack[i] == "-":
        #print("C")
        flips += 1
    elif i == 0:
      #print("A")
      current_run = stack[i]
      continue
    elif stack[i] == current_run:
      #print("D")
      continue
    else:
      #print("E")
      current_run = stack[i]
      flips += 1
      continue
  #print("F flips = ")
  return flips



if __name__ == "__main__":
  testcases = input()
  for caseNr in xrange(1, testcases+1):
    test_cast = raw_input()
    print("Case #%i: %s" % (caseNr, solve(test_cast)))
