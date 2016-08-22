for tc in range(input()):
	initial = raw_input()
	flip_count = 0
	pancakes = len(initial)
	if initial[pancakes-1] == "-":
		flip_count += 1
	for pancakes in range(pancakes - 1, 0, -1):
			if initial[pancakes-1] != initial[pancakes]:
				flip_count += 1
	print "Case #%d: %d" % (tc + 1, flip_count)