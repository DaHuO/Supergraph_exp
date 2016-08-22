def solve(s):
	ans = s[0]
	for i in range(1, len(s)):
		if s[i] >= ans[0]:
			ans = s[i] + ans
		else:
			ans = ans + s[i]
	return ans

def main():
	infile = open("A-large.in", "r")
	output = open("A-large.out", "w")
	T = int(infile.readline())
	for i in range(1, T+1):
		s = infile.readline()
		print("Case #%d: %s" % (i, solve(s)), file = output, end= "")
main()
