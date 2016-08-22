filename = "C:\\Users\\Adarsh\\Documents\\Google codejam\\2016\\round 1\\input.txt"
outputfilename= "C:\\Users\\Adarsh\\Documents\\Google codejam\\2016\\round 1\\output.txt"
file = open(filename)
output = open(outputfilename, 'w')
T=int(file.readline())
for x in range(0,T):
	S=file.readline()
	S = S.strip(' \t\n\r')
	for i in range(0,len(S)):
		if i==0:
			word=S[i]
		else:
			if S[i]>=word[0]:
				word=S[i]+word
			else:
				word=word+S[i]
	output.write("Case #"+str(x+1)+": "+word+"\n")