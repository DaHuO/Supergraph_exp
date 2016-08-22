import sys
import numpy as np

def solve(pancake_stack):
    movements_counter = 0
    stop = False
    while not stop:
      limit = np.where(pancake_stack==0)[0]
      if len(limit) == 0:
        stop = True
      else:
        limit = limit[-1]+1
        pancake_stack[:limit] = (1+pancake_stack[:limit])%2
        movements_counter += 1
    return movements_counter


if __name__ == '__main__':
    f_in = open('B-large.in', 'r')
    f_out = open('out_large.txt', 'w')
    cases = int(f_in.readline())
    for i in xrange(cases):
        pancake_stack = f_in.readline()[:-1]
        pancake_stack = pancake_stack.replace('-','0') # 0 means upside down
        pancake_stack = pancake_stack.replace('+','1')
        movements = solve(np.array(list(pancake_stack), dtype=np.uint8))
        f_out.write('Case #' + str(i+1) + ": " + str(movements) + "\n")
