t = int(raw_input())
for x in xrange(1,t+1):
	print "Case #{}:".format(x),
	str= raw_input()
	str1 = ""
	for y in xrange(0, len(str)):
		if str1 + str[y] > str[y]+str1:
			str1 = str1 + str[y]
		else:
			str1 = str[y] + str1
	print str1