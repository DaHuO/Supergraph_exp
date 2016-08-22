f = open('B-large.in', 'r')

T = f.readline()

output = open("pancakes.txt", 'w')

i = 1
for line in f:
	ans = 0
	for c in range(0,len(line)-2):
		if line[c] != line[c+1]:
			ans = ans + 1
	if line[len(line)-2] == '-':
		#print('hi' + line)
		ans = ans + 1
	output.write('Case #' + str(i) + ': ' + str(ans) + '\n')
	i = i + 1