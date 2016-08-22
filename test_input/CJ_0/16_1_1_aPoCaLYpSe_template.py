import copy
import sys
import math

sys.setrecursionlimit(10000)

def parse_case(instrm):
	return instrm.readline().strip()
   
   
def solve_case(case):
	if len(case) <= 0:
		return case
	rec = solve_case(case[1:])
	sol1 = case[0] + rec
	sol2 = rec + case[0]
	return max(sol1, sol2)



if __name__ == "__main__":
	instrm = open(sys.argv[1])
	ncases = int(instrm.readline().strip())
	for i in range(ncases):
		case = parse_case(instrm)
		ans = solve_case(case[::-1])
		print("Case #{}: {}".format(i+1, ans))
