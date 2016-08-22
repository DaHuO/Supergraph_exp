#!/usr/bin/env python3

import sys


def parse_stack(s):
  return [1 if p == "+" else -1 for p in s]


def flip(stack, i):
  return [p * -1 for p in stack[:i]] + stack[i:]


def solve(stack):
  flip_count = 0
  while -1 in stack:
    stack = flip(stack, len(stack) - stack[::-1].index(-1))
    flip_count += 1
  return flip_count


if __name__ == "__main__":
  input_filepath = sys.argv[1]

  with open(input_filepath, "rt") as input_file:
    T = int(next(input_file))

    for i in range(1, T + 1):
      stack = parse_stack(next(input_file).strip())
      print("Case #%u: %u" % (i, solve(stack)))

    assert(i == T)
