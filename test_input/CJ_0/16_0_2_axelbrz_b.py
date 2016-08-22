from Queue import Queue

f = open("b.in")
d = f.read().strip().split("\n")[1:]
f.close()

def bfs(input):
	if not "-" in input: return 0
	q = Queue()
	q.put((input, 0))
	used = set([input])
	while not q.empty():
		cur, steps = q.get()
		maxlen = cur.rfind("-") + 1
		if maxlen == 0: return steps
		for i in xrange(maxlen + 1):
			adj = cur[:i][::-1].replace("-", "A").replace("+", "-").replace("A", "+") + cur[i:maxlen]
			if not "-" in adj: return steps + 1
			if not adj in used:
				q.put((adj, steps + 1))
				used.add(adj)
	return 0

o = open("b.out", "w")
for i in xrange(len(d)):
	input = d[i]
	
	s = bfs(input)
	ln = "Case #%d: %s" % (i + 1, s)
	print ln
	o.write(ln + "\n")
o.close()
