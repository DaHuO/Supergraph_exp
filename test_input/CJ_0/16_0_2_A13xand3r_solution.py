def readandwritefile(file):
	with open(file) as f:
		lines = f.readlines()
		numcases = int(lines[0].rstrip())
		linestowrite = []
		for i in range(1, (numcases+1)):
			linestowrite.append(solve(lines[i].rstrip().split()))
		writeanswer(linestowrite, 'file.out')
		f.close()

def writeanswer(lines, file):
	with open(file, 'w+') as f:
		for i in range(0 ,len(lines)):
			line = lines[i]
			f.write("Case #" + str(i+1) + ": " + line)
			if(i+1 < len(lines)):
				f.write("\n")
		f.close()











def solve(params):
	stack = params[0]
	timesflipped = 0
	for i in range(0, len(stack)):
		if(i > 0 and stack[i] != stack[i-1]):
			timesflipped += 1
	if(stack[len(stack)-1] == "-"):
		timesflipped += 1
	return str(timesflipped)




readandwritefile('file.in')