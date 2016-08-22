#code jam - problem_b

n = int(raw_input())

for i in range(n):
	p = raw_input()
	n = 1
	t = len(p)
	
	for j in range(t - 1):
		if p[j] != p[j + 1]:
			n += 1
	if p[t - 1] == "+":
		n -= 1
			
	print "Case #%d: %d" %(i + 1, n)
