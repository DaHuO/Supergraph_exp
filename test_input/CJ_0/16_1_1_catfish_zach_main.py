def main():

	r_file = open('A-small-attempt0.in', 'r')
	w_file = open('output.txt','w')

	t = int(r_file.readline())

	for x in range(t):

		s = r_file.readline()[:-1]
		print s
		outputString = 'Case #{}: {}\n'.format(x + 1, lastWord(s))
		w_file.write(outputString)

	r_file.close(); w_file.close()

def lastWord(word, pivot = None):

	if len(word) == 1:
		if pivot == None: return word
		else:
			return sorted([word[0] + pivot, pivot + word[0]])[-1]

	else:

		if pivot == None:
			return lastWord(word[1:], pivot = word[0])

		nextLetter = word[0]

		return sorted([lastWord(word[1:], pivot = nextLetter + pivot),
			lastWord(word[1:], pivot = pivot + nextLetter)])[-1]

if __name__ == '__main__':
	main()