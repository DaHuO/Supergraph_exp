def run():
	i = 0
	with open('input.txt', 'rt') as src, open('output.txt', 'wt') as tgt:
		for line in src:
			line = line.rstrip('\r\n')
			if i > 0:
				print "Case #%d: %s" % (i, processItem(i, line))
				tgt.write("Case #%d: %s\n" % (i, processItem(i, line)))
			i = i + 1
			
def processItem(i, line):
	output = ""
	for letter in line:
		if(len(output) == 0):
			output = letter
		else:
			if(output[0] <= letter):
				output = letter + output
			else:
				output = output + letter
	return output
	
run()