
def lastWord(word):
	if len(word) == 1 or len(word) == 0:
		return word
	else:
		lastAlphabet = 'A'
		splitPoint =  0
		for i in xrange(len(word)):
			if word[i] >= lastAlphabet:
				splitPoint = i
				lastAlphabet = word[i]
		return word[splitPoint] + lastWord(word[0:splitPoint]) + word[splitPoint+1:]

T = int(raw_input())
for i in xrange(1,T+1):
	word = raw_input()
	print "Case #{}: {}".format(i, lastWord(word))
