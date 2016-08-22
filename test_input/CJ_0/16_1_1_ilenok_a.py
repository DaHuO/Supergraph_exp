def last_word(s):
	tmp = []
	for ch in s:
		if (len(tmp) == 0):
			tmp.append(ch)
		elif ord(tmp[0]) > ord(ch):
			tmp.append(ch)
		else: # ord(tmp[0]) < ord(ch):
			tmp.insert(0, ch)
	lw = ''.join(tmp)	
	print lw
	return lw
	
		

inf = open("a.in", 'r')
outf = open("a.out", 'w')

t = int(inf.readline())


for k in xrange(0, t):
	s = inf.readline().strip()		
	outf.write("Case #" + str(k + 1) + ": ")	
	outf.write(last_word(s) + "\n")
outf.close()
