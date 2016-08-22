#!/bin/python

def CollapsePancakes(p):
	result=p[0]
	while p != "":
		if p[0] != result[-1]:
			result+=p[0]
		p = p[1:]
	return result

def FlipPancakes(p):
	answer=""
	for c in p:
		if c =="+":
			answer+="-"
		else:
			answer+="+"
	return answer

def CountPancakeFlips(p):
	p = CollapsePancakes(p)
	if p == "+":
		return 0
	elif p == "-":
		return 1
	elif p == "-+":
		return 1
	elif p == "+-":
		return 2
	else:
		if p[-1] == "+": # ******+
			return CountPancakeFlips(p[0:-1])
		else: # p[1] == "-": # -*****-
			return 1 + CountPancakeFlips(FlipPancakes(p)) # Flip all pancakes to count


t = int(raw_input())

for i in xrange(1, t + 1):
	n = raw_input()
	o = CountPancakeFlips(n)
	print "Case #{}: {}".format(i, o)