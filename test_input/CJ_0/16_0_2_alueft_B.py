t = int(raw_input())
for T in xrange(t):
  s = raw_input()
  while s and s[-1] == "+":
    s = s[:-1]
  x = 0
  while s:
    while s and s[-1] == "-":
      s = s[:-1]
    x += 1
    if not s:
      break
    while s and s[-1] == "+":
      s = s[:-1]
    x += 1
    if not s:
      break
  print "Case #{0}: {1}".format(T+1,x)
