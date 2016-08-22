#!/usr/bin/env python

flip_map = {'-': '+', '+': '-'}
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def happy_side_up(stack):
  count = 0
  for each in range(len(stack)):
      if '-' not in stack:
        break
      elif '+' not in stack:
        count += 1
        break
      index = stack.find(flip_map[stack[0]])
      stack = stack[index] * index + stack[index:]
      count += 1
  return count


t = int(raw_input())  # read a line with a single integer

for case in xrange(1, t + 1):
  s = str(raw_input())
  return_value = happy_side_up(s)
  print "Case #{}: {}".format(case, return_value)
  # check out .format's specification for more formatting options
