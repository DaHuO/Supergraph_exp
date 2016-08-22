def ltn(letter):
	c={
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    'E': 5,
	'F': 6,
	'G': 7,
	'H':8,
	'I':9,
	'J':10,
	'K': 11,
	'L':12,
	'M':13,
	'N':14,
	'O':15,
	'P':16,
	'Q':17,
	'R':18,
	'S':19,
	'T':20,
	'U': 21,
	'V': 22,
	'W': 23,
	'X':24,
	'Y':25,
	'Z':26}
	return c[letter]
def lwgen(word):
	lw = word[0]
	for l in range(len(word)-1):
		le = word[l+1]
		la = lw[0]
		if ltn(le)>=ltn(la):
			lw =le+lw
		else:
			lw=lw+le
	return lw
infile = open("/root/Desktop/infile.txt")
outfile = open("/root/Desktop/outfile.txt", "w")
line1 = int(infile.readline())
for case in range(line1):
	s = infile.readline().split('\n')[0]
	oc = lwgen(s)
	casenum = case + 1
	outfile.write("Case #%s:"% casenum+" "+oc+"\n")
infile.close()
outfile.close()
