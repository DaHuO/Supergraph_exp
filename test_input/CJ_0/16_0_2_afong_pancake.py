from sys import argv

with open(argv[1], 'r') as of:
	cases = int(of.next())
	for n, x in enumerate(of):
		stack = []
		for side in x.strip().split():
			stack += side
		lastcake = stack[0]
		flips = 0
		for cake in stack:
			if cake != lastcake:
				lastcake = cake
				flips += 1
		if stack[-1] != '+':
			flips += 1
		print('Case #' + str(n+1) + ': ' + str(flips))
	