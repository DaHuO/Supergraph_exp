def solve(s):
	ans = []
	ans.append(s[0])
	for i in range(1,len(s)):
		c = s[i]
		if ord(c) >= ord(ans[0]):
			ans.insert(0,c)
		else:
			ans.append(c)
	return "".join(ans)



f = open("A-large.in")
T = int(f.readline())
for case in range(1,T+1):
	if case != T:
		print "Case #" + str(case) +": " + solve(f.readline()[0:-1])
	else:
		print "Case #" + str(case) +": " + solve(f.readline())

