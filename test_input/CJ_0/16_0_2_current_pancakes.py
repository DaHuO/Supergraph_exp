import sys

def flip_pancakes(filename):
  with open(filename) as f:
    T = int(f.readline().rstrip())
    for t in range(T):
      stack = f.readline().rstrip()
      # print 'old stack',stack
      pnum = len(stack)-1
      flip_count = 0
      while '-' in stack and pnum >= 0:
        if stack[pnum] == '-':
          stack = stack[:pnum+1].replace('-','a').replace('+','-').replace('a','+') + stack[pnum+1:]
          # print stack
          flip_count += 1
          # print 'new stack',stack
        pnum -= 1
      print "Case #{}: {}".format(t+1, flip_count)

if __name__ == '__main__':
  flip_pancakes(sys.argv[1])