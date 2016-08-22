def decideLastWord(case):
	chrs = list()	
	for a in case:		
		if len(chrs) == 0:
			chrs.append(a)
			continue
		
		curr = chrs[0]		
		if ord(a)<ord(curr):
			chrs.append(a)
		else:
			chrs.insert(0,a)
	return "".join(chrs)
	
def main():
	testCount = raw_input()
	testCases=list()
	for i in range (0,int(testCount)):
		testCase = raw_input()
		testCases.append(testCase)
	
	for i in range(0,len(testCases)):
		result = decideLastWord(testCases[i])
		print "Case #"+str(i+1) + ": " + str(result)
		

main()