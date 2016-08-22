import sys

N = int(sys.stdin.readline().strip())

for qw in range(1,N+1):
	string = sys.stdin.readline().strip()
	s = ""
	for char in string:
		if s == "":
			s= char
		elif char<s[0]:
			s = s+char
		else:
			s = char+s
	print("Case #%d: %s"%(qw,s))