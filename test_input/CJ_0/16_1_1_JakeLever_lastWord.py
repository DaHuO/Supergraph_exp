import sys
import fileinput

def lastWord(S):
	letters = sorted(list(set(S)))
	if len(letters) < 1:
		return S
	
	lastLetter = letters[-1]
	firstInstance = S.find(lastLetter)
	lastCount = S.count(lastLetter)
	
	repLetters = [ lastLetter for _ in xrange(lastCount) ]
	repLetters = "".join(repLetters)
	endBit = S[firstInstance:].replace(lastLetter,'')
	
	beforeLastLetter = S[:firstInstance]

	return repLetters + lastWord(beforeLastLetter) + endBit

caseCount = None
for i,line in enumerate(fileinput.input()):
	line = line.strip()
	if caseCount is None:
		caseCount = int(line)
	else:
		print "Case #%d: %s" % (i, lastWord(line))

