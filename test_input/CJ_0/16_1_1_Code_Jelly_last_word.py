import cProfile, pstats, io, getopt, sys

def getLastWord(inStr):
	if len(inStr) == 1:
		return inStr
	outStr=inStr[0]
	for char in inStr[1:]:
		if char >= outStr[0]:
			outStr = char + outStr
		else:
			outStr = outStr + char
	return outStr

def mainLogic(numCases, inFile):
	output=""
	for case in range(numCases):	
		result = getLastWord(inFile.readline().strip())
		output = output+"Case #{}: {}\n".format(case+1,result)
	return output

inPath=""
try:
	opts, args = getopt.getopt(sys.argv[1:],"hi:")
except getopt.GetoptError:
	print('Use -i to specify an input file')
	sys.exit(1)
for opt, arg in opts:
	if opt == '-h':
		print('Use -i to specify an input file')
		sys.exit()
	elif opt == '-i':
		inPath = arg
if inPath=="":
	inPath='test.in'
pr = cProfile.Profile()
pr.enable()
inFile = open(inPath,'rU')
outFile = open(inPath.replace('.in','')+'.out','w')
numCases = int(inFile.readline())
output = mainLogic(numCases, inFile)
outFile.write(output)
inFile.close()
outFile.close()
pr.disable()
s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
