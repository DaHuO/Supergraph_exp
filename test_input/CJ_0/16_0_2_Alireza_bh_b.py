import Queue as Q
T = input()

graph = {}

def trim(s):
	while len(s)>0 and s[-1]=='+':
		s = s[:-1]
	return s


for mask in range(2**10):
	t = mask
	s = ""
	while t > 0:
		if t%2 == 1: s = s + '-'
		else: s = s + '+'
		t/=2
	graph[s] = []
	for i in range(len(s)):
		tS = s[i::-1]
		tS = tS.replace('+','p').replace('-','+').replace('p','-')
		newS = trim(tS+s[i+1:])
		if not newS in graph: graph[newS] = []
		graph[newS].append(s)
		graph[s].append(newS)

d = {}
d[""] = 0
visited = {}
q = Q.Queue()
visited[""] = True
q.put("")

while not q.empty():
	v = q.get()
	for u in graph[v]:
		if not u in d: d[u]=1000*1000
		d[u] = min(d[u],d[v]+1)
		if not u in visited:
			visited[u] = True
			q.put(u)

for case in range(1,T+1):
	s = raw_input()
	ans = d[trim(s)]
	print "Case #{}: {}".format(case,ans)
	
