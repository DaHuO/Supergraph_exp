import sys

def get_last_word(filename):
  with open(filename, 'r') as f:
    T = int(f.readline().rstrip())
    for t in xrange(T):
      s = f.readline().rstrip()
      out = s[0]
      for i in xrange(1, len(s)):
        if s[i] >= out[0]:
          out = s[i] + out
        else:
          out += s[i]
      print "Case #{}: {}".format(t+1, out)

if __name__ == '__main__':
  get_last_word(sys.argv[1])