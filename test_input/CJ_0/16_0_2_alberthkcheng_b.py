n = int(raw_input())

def get_min_move(s):
	move = 0

	pie = map(lambda x : x == '+', list(s))
	pie.append(True)
	last = pie[0]
	for i in range(1, len(pie)):
		if last != pie[i]:
			move += 1
			last = pie[i]

	return move


for i in range(n):
	s = raw_input()
	print "Case #" + str(i+1) + ": " + str(get_min_move(s))