def flip(s):
	n = ""
	for i in range(len(s)):
		if s[i] == "+":
			n += "-"
		else:
			n += "+"
	return n

def f(s):
	x = s[::-1]
	count = 0
	while x != "+"*len(s):
		for i in range(len(x)):
			if x[i] == "-":
				x = x[0:i] + flip(x[i:])
				count += 1
				break
	return count

x = raw_input()
for i in range(int(x)):
	a = raw_input()
	print "Case #%s: %s" % (i+1, f(a))