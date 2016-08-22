with open("input11","r") as f:
	T = f.readline().strip()
	i=0
	for line in f:
		i=i+1
		s = line[0]
		for l in line[1:]:
			if l < s[0]:
				s = s+l
			else:
				s = l+s

		#print "Case #{}: {}".format(i,s.strip())
		with open("output1","a+") as g:
			g.write("Case #{}: {}".format(i,s))