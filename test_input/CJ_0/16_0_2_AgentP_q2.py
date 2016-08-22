def revert(s):
	a = ""
	for x in s:
		if(x=="+"):
			a+="-"
		elif(x=="-"):
			a+="+"
	return a

def func(s):
	if(s=="-"):
		return 1
	elif(s=="+"):
		return 0
	elif(s[len(s)-1:] == "+"):
		return func(s[:len(s)-1])
	elif(s[len(s)-1:] == "-"):
		return 1+func(revert(s[:len(s)-1]))

t = range(int(raw_input()))
for i in t:
	s = raw_input()
	print "Case #"+str(i+1)+": "+str(func(s))