fp = open('A-small.in','r')
fw = open('A-small.out','w')

cases = int(fp.readline().strip())

for case in xrange(1, cases+1):
	words = []
	s = fp.readline().strip()
	words.append(s[0])
	for i in xrange(1,len(s)):
		y = []
		for word in words:
			y.append(s[i] + word)
			y.append(word + s[i])
		words = y

	y = sorted(words)
	fw.write("Case #{0}: {1}\n".format(case, y[-1]))
