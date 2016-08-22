t = int(input())
case = 0

while t:
	t -= 1
	case += 1
	s = input()
	lw = []
	for i in s:
		if lw == []:
			lw.append(i)
		else:
			if i < lw[0]:
				lw.append(i)
			else:
				lw = [i] + lw
	lw = ''.join(lw)
	print('Case #', case, ':', sep='', end = ' ')
	print(lw)