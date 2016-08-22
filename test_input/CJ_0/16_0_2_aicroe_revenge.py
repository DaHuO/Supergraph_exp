
def countFlips(pancakes):
	if len(pancakes) == 0:
		return 0
	count = 0
	ant = pancakes[0]
	for p in pancakes:
		if ant != p:
			count += 1
			ant = p
	if ant == '-':
		count += 1
	return count


T = int(raw_input())
for i in xrange(1, T + 1):
	print 'Case #{}: {}'.format(i, countFlips(raw_input()))

