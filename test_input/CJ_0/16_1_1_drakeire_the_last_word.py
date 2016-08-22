#!/usr/bin/env python3

import sys
from collections import deque

def main():
  fi = sys.stdin
  fo = sys.stdout
  case_count = int(fi.readline().strip())
  for i in range(1, case_count+1):
    word = read_input(fi)
    solution = solve(word)
    display_and_clear(fo, i, solution)

def read_input(f):
  return f.readline().strip()

def display_and_clear(f, i, solution):
  f.write('Case #%d: %s\n' % (i, solution))
  f.flush()

def solve(word):
  lasts = deque([word[0]])
  for i in range(1, len(word)):
    ch = word[i]
    if front_insertable(lasts, ch):
      lasts.appendleft(ch)
    else:
      lasts.append(ch)

  return ''.join(lasts)

def front_insertable(lasts, ch):
  index = 0
  while index < len(lasts):
    if ch < lasts[index]:
      return False
    elif ch > lasts[index]:
      return True
    else:
      index += 1

  # lasts == n * [ch], doesn't matter
  return False

if __name__ == '__main__':
  main()

