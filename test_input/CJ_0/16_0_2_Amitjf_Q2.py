def flip(lst, ind):
	return map(lambda x: not x, lst[ind - 1::-1]) + lst[ind::]

with open('B-large.in', 'r') as f:
	with open('output.txt', 'w') as f_out:
		n = int(f.readline())
		for i in range(n):
			line = f.readline().strip()
			lst_fin = map(lambda x: x=='+', line)
			lst = [True]*len(lst_fin)
			count = 0
			for j in range(len(lst)):
				if lst[-(j+1)] != lst_fin[-(j+1)]:
					count += 1
					lst = flip(lst, len(lst) - j)
			f_out.write('Case #' + str(i + 1) + ': ' + str(count) + '\n')