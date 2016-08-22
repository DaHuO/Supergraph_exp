def main():
	for TEST in xrange(1, int(raw_input())+1):
		S = raw_input()[::-1]
		flipped = False
		nFlips = 0

		for c in S:
			if flipped:
				if c == '-':
					c = '+'
				elif c == '+':
					c = '-'

			if c == '-':
				nFlips += 1
				flipped = not flipped

		print "Case #%d: %s" % (TEST, str(nFlips))

main()
