def solve(s):
  c = 0
  N = len(s)
  for i in xrange(1,N):
    if s[i] != s[i - 1]:
      c += 1
  if s[N - 1] == '-':
    c += 1
  return c

T = int(input())
for i in xrange(T):
  s = raw_input()
  print "Case #%d: %d" %(i + 1, solve(s))
