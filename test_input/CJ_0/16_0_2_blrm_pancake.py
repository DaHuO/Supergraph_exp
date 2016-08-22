#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def _is_happy(cake_stack):
  """ Returns True if entire stack is Happy-side up, False otherwise.
  """
  if re.search('^\++$', cake_stack) is not None:
    return True
  else:
    return False

def _is_sad(cake_stack):
  """ Returns True if entire stack is sad-side up, False otherwise.
  """
  if re.search('^\-+$', cake_stack) is not None:
    return True
  else:
    return False

def _flip_section(cake_stack, slice_index):
  result = cake_stack[:slice_index].replace('-','!').replace('+','-').replace('!','+')[::-1] + cake_stack[slice_index:]
  return result

def flip_cakes(cake_stack):
  """ This function takes a string of - and + as input
      and returns minimum number of flips required to
      orient the whole stack +-side up. Flips can only
      occur from the left-side.
  """
  cakes = cake_stack[:]
  num_flips = 0
  while _is_happy(cakes) is False:
    # print cakes
    num_flips += 1
    if _is_sad(cakes):
      cakes = _flip_section(cakes, len(cakes))
      break
    elif cakes[0] == '-':
      cakes = _flip_section(cakes, cakes.find('-+') + 1)
    elif cakes[0] == '+':
      cakes = _flip_section(cakes, cakes.find('+-') + 1)
  return num_flips


if __name__ == "__main__":
  testcases = input()
  for caseNr in xrange(1, testcases+1):
    cakestack = raw_input()
    print("Case #%i: %s" % (caseNr, flip_cakes(cakestack)))
