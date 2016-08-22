for i in range(int(input())):
	s = input()
	res = []
	for c in s:
		if len(res) == 0 or c >= res[0]:
			res = [c] + res
		else:
			res.append(c)
	print('Case #{}: {}'.format(i+1, ''.join(res)))
