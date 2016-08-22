def solving(line):
	pancakes = []
	for c in line:
		if c == '-' or c == '+':
			pancakes.append(c)	
	pos,neg = flip(pancakes)

	return pos

def flip(cakes):
	if len(cakes) == 0:
		return (0,0)
	pos,neg = flip(cakes[:-1])
	if cakes[-1] == '+':
		return (min(pos,neg+1), min(pos+1,neg+2))
	else:
		return (min(neg+1,pos+2), min(neg, pos+1) )

with open('input', 'r') as input:
	count = 0
	for line in input:
		if count == 0:
			count+=1
			continue
		print 'Case #%d: %s' % (count, solving(line))
		count+=1