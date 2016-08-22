def inputvars():
	f = open('input.txt')
	num = int(f.readline())
	numlist = f.read().splitlines()
	return num, numlist

def outputvars(num, output):
	f = open('output.txt', 'w')
	for x in range(num):
		f.write(str('Case #' + str(x + 1) + ': ' + str(output[x]) + '\n'))
	f.close()

def reverse(string, end):
	# print(string, ' ', end)
	# print('Original String: ', string[:end])
	for x in range(end):
		if(string[x] == '-'):
			string[x] = '+'
		else:
			string[x] = '-'
	# print('Flipped String: ', string[end - 1::-1])
	string[:end] = string[end - 1::-1]
	# print('string: ', string)
	return string

def main():
	num, numlist = inputvars()
	output = []
	for x in range(num):
		curstring = list(numlist[x])
		# print(curstring)
		iterations = 0
		# if(curstring.count('-') > len(curstring) / 2):
		# 	curstring = reverse(curstring, len(curstring))
		# 	# print(curstring, 'Entered 1, ', iterations, '\n')
		# 	iterations += 1
		# if(curstring.count(curstring[0]) <= len(curstring) / 2):
		# 	curstring = reverse(curstring, 1)
		# 	print(curstring, 'Entered 2, ', iterations, '\n')
		# 	iterations += 1
		for curnum in range(len(curstring)):
			if(not curstring[0] == curstring[curnum]):
				numflip = curnum
				while(numflip < len(curstring) and curstring[curnum] == curstring[numflip]):
					numflip += 1
				# print(numflip)
				curstring = reverse(curstring, curnum)
				# print(curstring, 'Entered 3, ', iterations, '\n')
				iterations += 1
				if(curstring.count('-') > 0):
					curstring = reverse(curstring, numflip)
					# print(curstring, 'Entered 4, ', iterations, '\n')
					iterations += 1
		if(curstring[curnum] == '-'):
			reverse(curstring, len(curstring))
			# print(curstring, 'Entered 5, ', iterations, '\n')
			iterations += 1
		# print(x + 1, ': ', curstring, '\n\n\n')

		output.append(iterations)
	outputvars(num, output)

main()