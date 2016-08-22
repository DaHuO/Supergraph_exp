# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io

def fixedBin(x, d):
	s = bin(x)[2:]
	if(len(s) < d):
		s = '0'*(d-len(s)) + s
	return s

def getPrefixes(d):
	if d <= 2:
		return ['1'*d]
	return ['1' + fixedBin(x, d-2) + '1' for x in xrange(0, 2**(d-2))]

def baseFacts(s):
	return [sum(int(d)*k**i for i,d in enumerate(s[::-1])) for k in xrange(2, 11)]

# Using algebraic grouping: repeating a pattern at the beginning and end of the string guarantees non-primality in all bases
# So we do this with all palindromic sequences starting and ending with 1
def getAlgFacStrings(n):
	solns = []
	for d in xrange(2, 1+n//2):
		solns.extend([[x + '0'*(n-2*d) + x]+ baseFacts(x) for x in getPrefixes(d)])
	return solns

def solve_case(s):
	N = s[0]
	J = s[1]
	Str = getAlgFacStrings(N)
	return Str[:J]


def solve(fin, fout):
	L = codejam_io.read_simple(fin)
	S = map(solve_case, L)
	codejam_io.write_slst(fout, S)

#solve("C-sample.in", "C-sample.out")
#solve("C-small-will-be.in", "C-small-will-be.out")
#solve("C-large-will-be.in", "C-large-will-be.out")
#solve("C-small-attempt0.in", "C-small-attempt0.out")
solve("C-large.in", "C-large.out")