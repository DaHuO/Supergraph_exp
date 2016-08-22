def flip(string, pos):
	tran = {"+":"-","-":"+"}
	return "".join(tran[i] for i in reversed(string[:pos])) + string[pos:]

def count(l, check = "+"):
	i = 0
	while "-" in l and check in l:
		i += 1
		for k, c in enumerate(l):
			if c == check:
				l = flip(l, k)
				break
		check = tran[check]
	if check == "+" and "-" in l:
		l = flip(l, len(l))
		i += 1
	return i

with open("B-small-attempt0.in", "r") as f:
	i = 1
	tran = {"+":"-","-":"+"}
	i = 0
	for l in f.read().split("\n")[1:]:
		ori = l
		if len(l) > 0:
			i += 1
			print "Case #{}: {}".format(str(i), str(min(count(l, "+"), count(l, "-"))))