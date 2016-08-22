import sys
import numpy as np

def solve(S):
  last_word = ''
  leftmost_char = ''
  for c in S:
    if last_word == '':
      last_word = c
      leftmost_char = c
    else:
      if c >= leftmost_char:
        last_word = c + last_word
        leftmost_char = c
      else:
        last_word = last_word + c
  return last_word


if __name__ == '__main__':
  f_in = open('A-large.in', 'r')
  f_out = open('out_large.txt', 'w')
  cases = int(f_in.readline())
  for i in xrange(cases):
    S = f_in.readline()[:-1]
    last_word = solve(S)
    f_out.write('Case #' + str(i+1) + ": " + str(last_word) + "\n")
