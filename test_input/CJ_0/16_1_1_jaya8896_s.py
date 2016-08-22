def solve(st):
	global answer
	new = ''
	new += st[0]
	st = st[1:]
	for item in st:
		if item>=new[0]:
			new = item + new
		else:
			new += item
	answer = new
	


for cases in range(input()):
	st = raw_input()
	answer = ' '
	solve(st)
	print "Case #" + str(cases+1) + ": " + answer