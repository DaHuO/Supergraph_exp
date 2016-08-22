T = input()
outputs = []
for i in range(T):
	current = raw_input()
	pivot = current[0]
	last_word = ''
	for i in current:
		if(i < pivot):
			last_word = last_word + i
		else:
			last_word = i + last_word
			pivot = i
	outputs.append(last_word)
count = 1
for i in outputs:
	print 'CASE #{}: {}'.format(count, i)
	count += 1