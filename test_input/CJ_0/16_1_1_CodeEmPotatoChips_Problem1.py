fp = open("C:\\Users\\atifh\\Desktop\\A-large.in", "r")
fp2 = open("Output.txt", "w")
lines = fp.readlines()
t = int(lines[0])
count = 0
for i in range(1, t+1):
	string = lines[i][0]
	for j in range(1, len(lines[i])):
		if lines[i][j] >= string[0]:
			string = lines[i][j]+string
		else:
			string+= lines[i][j]
	count+=1
	print("Case #"+str(count)+": "+string)
