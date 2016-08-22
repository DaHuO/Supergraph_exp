n = int(raw_input())

def get_largest_string(S):
	l = list()
	for s in S:
		if len(l) == 0:
			l.append(s)
		elif s < l[0]:
			l.append(s)
		else:
			l.insert(0, s)
	return "".join(l)

for i in range(n):
	s = list(raw_input())
	print "Case #" + str(i+1) + ": " + get_largest_string(s)