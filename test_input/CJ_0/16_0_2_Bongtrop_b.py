
t = int(raw_input(""))

for i in range(t):
	s = raw_input("").replace("\n", "").replace("\r", "")
	l = s[0]
	res = 0
	for j in range(1, len(s)):
		if l!=s[j]:
			res+=1
			
		l = s[j]
			
	if s[-1]=='-':
		res+=1
	
	print "case #"+str(i+1)+": "+str(res)

