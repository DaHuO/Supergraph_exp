with open('pancake.in') as f:
	data = f.read().split('\n')

with open('pancake.out', 'w') as f:
	for i in range(1, len(data)):
		row = data[i]
		count = 0
		is_plus = True
		for c in reversed(row):
			if c == '-' and is_plus:
				is_plus = False
				count += 1
			elif c == '+' and not is_plus:
				is_plus = True
				count += 1
		f.write('Case #{}: {}\n'.format(i, count))