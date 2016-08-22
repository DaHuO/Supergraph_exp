for case in range(1, int(input())+1):
	S = input()
	result = ""
	first = S[0]
	for c in S:
		if c >= first:
			result = c + result
			first = c
		else:
			result = result + c
	print ("Case #%d: %s" % (case,result))

