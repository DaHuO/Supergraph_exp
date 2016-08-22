#!/usr/bin/python2.7
# codejam.py

import string

H = '+'
E = '-'
maneuver = string.maketrans('+-', '-+')

T = int(raw_input())

def flipper(pancakes, total):
  if E not in pancakes:
    return total # no empty pancakes, done
  lowest = pancakes.rindex(E) # find lowest empty pancake in stack
  if lowest == 0: # if on top of stack, simple choice
    return total + 1
  else:
    return flipper(pancakes[:lowest+1].translate(maneuver), total+1)

for case_nbr in xrange(1, T+1):
  solution = flipper(raw_input(), 0)
  print "Case #{}: {}".format(case_nbr, solution)
