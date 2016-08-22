t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  s = raw_input()  # read a list of integers, 2 in this case
  out = []
  out.append(s[0])
  for c in s[1:]:
	if c >= out[0]:
		out.insert(0,c)
	else:
		out.append(c)
  print "Case #{}: {}".format(i, ''.join(out))
  # check out .format's specification for more formatting options