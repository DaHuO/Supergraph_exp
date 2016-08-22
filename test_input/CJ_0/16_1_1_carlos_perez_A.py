T = input()

for testCase in xrange(1, T + 1):
	letters = list(raw_input())
	lastWord = list(letters[0])
	highestChar = letters[0]

	for i in xrange(1, len(letters)):
		if letters[i] >= highestChar:
			lastWord = [letters[i]] + lastWord
			highestChar = letters[i]
		else:
			lastWord = lastWord + [letters[i]]

	print 'Case #{}: {}'.format(testCase, ''.join(lastWord))