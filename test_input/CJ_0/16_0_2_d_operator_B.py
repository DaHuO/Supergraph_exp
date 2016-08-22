# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io

def greedy_1(P):
	if 0 not in P:
		return 0
	else:
		return 1 + greedy_1([1-z for z in P[:len(P)-P[::-1].index(0)]])

def solve_case(s):
	P = [1 if ch == '+' else 0 for ch in s[0]]
	return greedy_1(P)

def solve(fin, fout):
	L = codejam_io.read_simple(fin, str)
	S = map(solve_case, L)
	codejam_io.write_simple(fout, S)

#solve("B-sample.in", "B-sample.out")
#solve("B-small-attempt0.in", "B-small-attempt0.out")
solve("B-large.in", "B-large.out")