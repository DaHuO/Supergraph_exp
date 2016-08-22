import string

t = int(raw_input())

for caseNumber in range(1, t + 1):
	s = raw_input()
	
	flip = 0
	flip += string.count(s,"+-") * 2
	if s.startswith("-"):
		flip += 1
	
	print "Case #{}: {}".format(caseNumber, flip)