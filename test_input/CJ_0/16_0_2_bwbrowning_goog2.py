import sys

lines = sys.stdin.readlines()

case_num = 1
for line in lines[1:]:
	line = line.rstrip()
	
	prev = line[0]
	flips = 0
	for i in range(len(line)):
		if line[i] != prev:
			flips = flips + 1
		prev = line[i]


	if prev == '-':
		flips = flips + 1
	print "Case #%d: %d" % (case_num, flips)
	case_num = case_num+1
