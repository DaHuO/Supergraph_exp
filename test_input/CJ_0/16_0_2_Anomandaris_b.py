def analyse(line):
	pancakes = strip(line)

	flips = 0
	while "-" in pancakes:
		print(pancakes)
		pancakes = flip(pancakes)
		print(pancakes)
		pancakes = strip(pancakes)
		flips += 1

	return str(flips)

def strip(pancakes):
	while pancakes and pancakes[-1] == "+":
		pancakes = pancakes[:-1]
	return pancakes

def flip(pancakes):
	return ((pancakes.replace("+","*")).replace("-","+")).replace("*","-");


def run(name):
	lines = [l for l in open(name + ".in", mode='r')]
	n = int(lines[0])
	
	out = open(name + ".out",mode='w')
	for i, line in enumerate(lines[1:]):
		answer = analyse(line[:-1])
		out.write("Case #" + str(i+1) + ": " + answer + "\n")
	out.close()

run("B-large")