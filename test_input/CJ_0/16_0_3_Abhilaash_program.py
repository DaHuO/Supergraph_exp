from math import sqrt
def inputvars():
	f = open('input.txt')
	num = int(f.readline())
	numlist = f.readline().split()
	return int(numlist[0]), int(numlist[1])

def outputvars(num, output):
	f = open('output.txt', 'w')
	f.write('Case #1:\n')
	for x in range(num):
		f.write(str(output[x]) + '\n')
	f.close()

def comp(num):
	for x in range(2, int(sqrt(num) + 1)):
		if(num % x == 0):
			return x
	return -1

def main():
	length, numcoins = inputvars()
	output = []
	numstring = ''.join(['1'] + ['0'] * (length - 2) + ['1'])
	curnum = int(numstring, 2)
	numstring = ''.join(['1'] + ['1'] * (length - 2) + ['1'])
	maxnum = int(numstring, 2)
	while len(output) < numcoins and curnum < maxnum:
		curlist = bin(curnum)[2:]
		outputstr = [curlist]
		for base in range(2, 11):
			num = int(curlist, base)
			factor = comp(num)
			if(factor == -1):
				break
			outputstr.append(str(factor))
		if(len(outputstr) > 9):
			# print(outputstr)
			output.append(' '.join(outputstr))
		curnum += 2
	# print(output)
	outputvars(numcoins, output)

main()