import cProfile, pstats, io, getopt, sys, math

def getPrimeBreakers(strCandidate, radix):
	candidate = int(strCandidate, radix)
	for test in range(3, int(math.sqrt(candidate))+1):
		if candidate % test == 0:
			return test
	return 0

def generateJamcoins(digits, count):
	result = ''
	numFound = 0
	for candidate in range((2**(digits-1))+1,(2**digits),2):
		primeBreakers = []
		success = True
		for radix in range(2,11):
			test = getPrimeBreakers(bin(candidate)[2:], radix)
			if test == 0:
				success = False
				break
			primeBreakers.append(str(test))
		if success:
			numFound += 1
			result += "{} {}".format(bin(candidate)[2:], ' '.join(primeBreakers))
			if numFound == count:
				return result
			else:
				result += '\n'
	return result

def mainLogic(numCases, inFile):
	output=""
	for case in range(numCases):	
		parameters = [int(s) for s in inFile.readline().strip().split()]
		result = generateJamcoins(parameters[0], parameters[1])
		output = output+"Case #{}:\n{}\n".format(case+1,result)
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
