def trunc(s):
	trunc = 0
	for v in range(1, len(s)+1):
		if s[-v] == '+':
			trunc += 1
		else:
			break
	if trunc == 0:
		return s
	else:
		ts = s[:-trunc]
	return ts
def groupcount(s):
	c = 0	
	if not s=='':
		if s[0] == '+':
			c+=1+groupcountp(s[1:], '+')
		elif s[0] == '-':
			c+=1+groupcountp(s[1:], '-')
	return c
def groupcountp(s, prev):
	c=0
	if not s=='':
		if s[0] == '+':
			if prev == '+':
				c+=groupcountp(s[1:], '+')
			elif prev == '-':
				c+=1+groupcountp(s[1:], '+')
		elif s[0] == '-':
			if prev == '-':
				c+=groupcountp(s[1:], '-')
			elif prev == '+':
				c+=1+groupcountp(s[1:], '-')
	return c
infile = open("/root/Desktop/infile.txt")
outfile = open("/root/Desktop/outfile.txt", "w")
line1 = int(infile.readline())
for case in range(line1):
	s = infile.readline().split('\n')[0]
	for x in s:
		if x == '+':
			oc = '0'
		else:
			oc = str(groupcount(trunc(s)))
			break
	casenum = case + 1
	outfile.write("Case #%s:"% casenum+" "+oc+"\n")
infile.close()
outfile.close()
