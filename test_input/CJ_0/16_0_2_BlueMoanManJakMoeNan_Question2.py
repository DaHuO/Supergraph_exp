T = input()
values = []
for i in range(T):
	values.append(raw_input())

count = 1
for value in values:
	value = value[::-1]
	continuous_blocks = 0
	current_val = ''
	started = False
	for j in value:

		if(j == '-' and not started):
			started = True
			current_val = '-'
			continuous_blocks += 1

		elif(j=='+' and started and current_val=='-'):
			current_val = '+'
			continuous_blocks += 1

		elif(j=='+' and started and current_val=='+'):
			x=10

		elif(j=='-' and started and current_val=='+'):
			current_val = '-'
			continuous_blocks += 1

		elif(j=='-' and started and current_val=='-'):
			x=10

	print 'Case #{}: {}'.format(count, continuous_blocks)
	count += 1

		
