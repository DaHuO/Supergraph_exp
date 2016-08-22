import fileinput
import logging
from itertools import *

logging.basicConfig(level=logging.DEBUG)

def find_answer(lines):
  ''' Find the answer for this question '''
  a_str = lines[0]
  alpha_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  result = ''
  for i in a_str:
    if result == '':
      result = i
    else:
      if alpha_list.index(result[0]) <= alpha_list.index(i):
        result = i + result
      else:
        result = result + i       
 
  return result

def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1
  n_lines = 1
  for i in xrange(0, n_tests):
    tc = lines[start_test:start_test+n_lines]
    logging.debug(tc)
    n = find_answer(tc)
    print 'Case #{}: {}'.format(i+1, n)
    start_test += n_lines

if __name__ == '__main__':
  main()