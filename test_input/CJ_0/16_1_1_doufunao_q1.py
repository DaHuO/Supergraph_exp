"""TODO: Describe the contents of the module here. (shgao)
"""

from google3.pyglib import app
from google3.pyglib import flags


# flags.DEFINE_string('name', 'default', 'description')


FLAGS = flags.FLAGS

def lastword(s):
  lw = ''
  for c in s:
    ns = gen_last_word(lw, c)
    lw = ns
  return lw


def gen_last_word(w, c):
  if not len(w):
    return c
  if w[0] <= c:
    return c + w
  else:
    return w + c


  """The last word"""

  # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  print "Case #{}: {}".format(i, lastword(n[0]))
  # check out .format's specification for more formatting options


