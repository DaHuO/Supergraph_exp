infile = open("C-small-attempt0.in", "r")
outfile = open("output.in", "w")

testCases = infile.readline()

args = infile.readline()

args = args.split()

coinLength = int(args[0])

coinsNeeded = int(args[1])

start = 2**(coinLength-1) + 1
end = (2**(coinLength)) - 1



def toBinary (num):
	return ("{0:b}".format(num))

	

def checkAll (binary):
	array = [0] * 9
	for base in range(2,11):
		array[base-2] = isPrime(int(binary, base))
	return array

def isPrime(num):
	for i in range(2,int(num**0.5 + 1)):
		if num % i == 0:
			return i

	return 0;	

outfile.write("Case #1:\n")

counter = 1
for num in range(start,end+1,2):
	divisorsList = checkAll(toBinary(num))
	if all(divisorsList):
		outfile.write(toBinary(num))
		for div in divisorsList:
			outfile.write(" " + str(div))
		outfile.write("\n")	

		counter += 1
		if counter > coinsNeeded:
			break
