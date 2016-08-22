def noSteps(pancakes):
	n = len(pancakes)
	if n == 0:
		return 0
	i = 0
	res = 0
	first = True 
	while i < n:
		if pancakes[i] == '-':
			while i < n and pancakes[i] == '-':
				i += 1
			if first:
				res += 1
				first = False
			else:
				res += 2
		else:
			first = False
			i += 1
	return res

t = input()
for i in range(1, t+1):
	pancakes = raw_input()
	res = noSteps(pancakes)
	print "Case #{0}: {1}".format(i, res)
	#print "Case #{0}: {1}, {2}".format(i, res, int(res)/n)
