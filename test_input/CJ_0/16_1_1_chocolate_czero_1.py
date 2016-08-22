f = open("A-large.out", "w")
with open("A-large.in", "r") as inf:
	t = int(inf.readline())
	for it in xrange(t):
		s = inf.readline().strip()
		new_s = s[0]
		for i in xrange(1,len(s)):
			if s[i] >= new_s[0]:
				new_s = s[i]+new_s
			else:
				new_s = new_s+s[i]
		f.write("Case #%d: %s\n"%(it+1,new_s))

f.close()