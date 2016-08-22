import sys

T = sys.stdin.readline().strip()

for i in xrange(int(T)):
	S = sys.stdin.readline().strip()
	#out = sorted(S, reverse=True)
	#out = "".join(out)
	out = ''
	for c in S:
		out = max(out+c, c+out)

	print "Case #%s: %s" % (i+1, out)
