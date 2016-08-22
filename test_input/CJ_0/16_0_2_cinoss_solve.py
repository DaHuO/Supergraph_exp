from collections import deque
filename = "in.01"
filename = "B-small-attempt0.in.txt"
test = 0
for s in open(filename).readlines()[1:]:
	test += 1
	print "Case #%d:" % test,
	s = s.strip()
	flip = {
		'+': '-',
		'-': '+'
	}
	# s = '--+-'
	t = '+' * len(s)
	depth = {s:0}
	q = deque([s])
	while t not in depth and len(q) > 0:
		x = q.popleft()
		for i in range(1, len(x)+1):
			y = ''.join(reversed([flip[k] for k in x[:i]])) + x[i:]
			if y not in depth:
				depth[y] = depth[x] + 1
				q.append(y)
	if t in depth:
		print depth[t]