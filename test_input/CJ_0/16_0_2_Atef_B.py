
inp = open("B-large.in")
T = int(inp.readline().strip())

for _t in xrange(T):
  s = inp.readline().strip()
  flips = 0
  for i in xrange(len(s) - 1, -1, -1):
    if (s[i] == "-" and flips % 2 == 0) or (s[i] == "+" and flips % 2 == 1):
      flips += 1
  ans = flips
  print "Case #%d: %s" % (_t + 1, str(ans))
