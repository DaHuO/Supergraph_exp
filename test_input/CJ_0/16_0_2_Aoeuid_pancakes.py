import sys

inFile = sys.argv[1]

def getSolution(stack):
	numInversions = 0

	for i in range(0, len(stack) - 1):
		if (stack[i] is not stack[i+1]):
			numInversions = numInversions + 1
	
	if (stack[len(stack) - 1] is '-'):
		print("adding")
		numInversions = numInversions + 1

	return numInversions

with open (sys.argv[1], 'r') as myInput:
	with open ("output.txt", 'w') as myOutput:
		for idx, line in enumerate(myInput):
			if (idx == 0):
				continue;
			sol = getSolution(line[:-1])
			
			myOutput.write("Case #" + str(idx) + ": " + str(sol) + "\n")
