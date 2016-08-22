# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	caseList = input().split("\n")
	for j in range(0, len(caseList)):
		#print("Current pile : " + caseList[j]) #current line
		currentPile = caseList[j]
		flips = 0
		for k in range(0, len(currentPile)-1):
			if(currentPile[k+1]!=currentPile[k]):
				flips += 1
		if currentPile[-1] == '-':
			flips += 1
		print("Case #{}: {}".format(j, flips))