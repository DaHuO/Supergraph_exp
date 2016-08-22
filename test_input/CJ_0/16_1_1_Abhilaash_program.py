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
		letters = list(numlist[x])
		lastword = [letters[0]]
		letters.pop(0)
		for letter in letters:
			if(letter >= lastword[0]):
				lastword.insert(0, letter)
			else:
				lastword.append(letter)
		output.append(''.join(lastword))
	outputvars(num, output)

main()