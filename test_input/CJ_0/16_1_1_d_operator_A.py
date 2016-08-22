# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io

def solve_case(c):
	c = c[0]
	sol = c[0]
	for L in c[1:]:
		if L >= sol[0]:
			sol = L + sol 
		else:
			sol = sol + L
	return sol

def solve(fin, fout):
	L = codejam_io.read_simple(fin, str)
	S = map(solve_case, L)
	codejam_io.write_simple(fout, S)

#solve("A-sample.in", "A-sample.out")
#solve("A-small-attempt0.in", "A-small-attempt0.out")
#solve("A-small-attempt1.in", "A-small-attempt1.out")
#solve("A-small-attempt2.in", "A-small-attempt2.out")
solve("A-large.in", "A-large.out")