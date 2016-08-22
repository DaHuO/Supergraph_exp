def main():
	T = input()
	for tt in range(T):
		S = raw_input()

		c = runs = 0
		p = len(S)
		running = True if S[0]=='-' else False
		
		while c<p:
			if S[c]=='+' and running:
				runs += 1
				running = False
			elif S[c]=='-' and not running:
				running = True
		
			c += 1

		if S[-1]=='-':
			runs += 1

		f = runs*2

		if S[0]=='-':
			f -= 1


		print 'Case #{0}: {1}'.format(tt+1, f)


main()
