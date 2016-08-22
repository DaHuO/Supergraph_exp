from string import maketrans
panc = "--+-"
count = 0

r = open("B-large.in", 'r')
r2 = open("B-large.out",'w')
caseNumber = 1
r.readline()

def transl(p):
	return p.translate(maketrans("-+", "01"))


def flip(p, n):
	pan = transl(p)
	st = ""
	for x in pan[0:n][::-1]:
		if x == "0":
			st += "1"
		if x == "1":
			st += "0"
	return st+pan[n:len(p)]

def stepsNeeded(pancakes):
	global count
	if pancakes[0] == "1":
		ct = 1
		while ct < len(pancakes) and pancakes[ct] == "1":
			ct += 1
		if ct == len(pancakes):
			return 0
		count += 1
		pancakes = flip(pancakes, ct)
	if pancakes[0] == "0":
		ct = len(pancakes)
		while ct > 0 and pancakes[ct-1] == "1":
			ct -= 1
		count += 1
		pancakes = flip(pancakes,ct)
	stepsNeeded(pancakes)
	
for l in r.readlines():
	r2.writelines("Case #" + str(caseNumber)+": ")
	line = l[0:-1]
	stepsNeeded(transl(line))
	r2.writelines(str(count)+"\n")
	count = 0
	caseNumber += 1

