import sys

filename = sys.argv[1]
with open(filename,'r') as fh:
    T = int(fh.readline().strip())
    for t in range(T):
		s = fh.readline().strip()
		o = [s[0]]
		for c in s[1:]:
			if c >= o[0]:
				o[:0] = [c]
			else:
				o.append(c)

		print "Case #%d: %s" % (t+1, ''.join(o))