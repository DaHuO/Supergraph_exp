t = int(raw_input())
for T in xrange(t):
  s = raw_input()
  a = [s[0]]
  for i in xrange(1,len(s)):
    if s[i] >= a[0]:
      a = [s[i]]+a
    else:
      a.append(s[i])
  print "Case #{0}: {1}".format(T+1,"".join(a))
