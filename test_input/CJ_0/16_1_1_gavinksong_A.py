import sys

sys.setrecursionlimit(2000)
filename = "A-large"

def solve(s) :
	if len(s) == 1 :
		return s
	head, tail = (solve(s[:-1]), s[-1])
	if head[0] > tail :
		return head + tail
	else :
		return tail + head

with open(filename + ".in.txt", "r") as input :
	with open(filename + ".out.txt", "w") as output :
		for case_num in range(1, int(input.readline()) + 1) :
			output.write("Case #{}: ".format(case_num))
			answer = solve(input.readline().rstrip())
			output.write("{}\n".format(answer))