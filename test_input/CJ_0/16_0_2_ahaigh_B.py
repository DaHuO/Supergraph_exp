import sys
import itertools
import string

def compress(s):
	t = ""
	prev = None
	for x in s:
		if x != prev:
			t = t + str(x)
		prev = x
	return t

seen = {}
def ans(s):
#	print s
	if s == "+":
		return 0
	if s in seen.keys():
		return seen[s]
	seen[s] = 1000
	r = 1000
	for i in xrange(0, len(s)+1):
		# flip the prefix [0,i)
		t = compress(''.join(["+" if x == "-" else "-" for x in reversed(s[0:i])]) + s[i:])
		r = min(r, 1 + ans(t))
	seen[s] = r
	return r

def main():
	s = sys.stdin.readline()
	T = int(s)
	for i in xrange(0,T):
		s = string.strip(sys.stdin.readline())
		print "Case #{0}: {1}".format(i+1, ans(compress(s)))

if __name__ == "__main__":
	main()
