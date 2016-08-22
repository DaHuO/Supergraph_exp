#!/usr/bin/env python

def changeSigns(stack):
	newstack = ""
	for i in stack:
		if i == "+":
			newstack += "-"
		elif i == "-":
			newstack += "+"
	return newstack
	
if __name__=="__main__":
	
	for i in range(int(raw_input())):
		
		S = raw_input().strip()
		steps = 0
		
		while "-" in S:
			# First Step: remove the trailing +s
			im = S.rfind("-")
			S = S[:im+1]
			
			# Second Step: do your work
			if S[0] == "-":
				sub, rest = S, ""
			else:
				j = S.rfind("+")
				sub, rest 	= S[:j+1], S[j+1:]
			sub = changeSigns(sub)
			sub = sub[::-1]
			S = (sub + rest).strip()
			steps += 1

		print("Case #%d: %d" % (i+1, steps))