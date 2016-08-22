t = int(input())
case = 0

while t:
	t -= 1
	case += 1
	flips = 0
	flag = 0
	p = input()
	pl = list(p)
	while pl.count('-') != 0:
		#print(pl, flips)
		if pl.count('+') == 0:
			flips += 1
			break
		plus_i = pl.index('+')
		minus_i = pl.index('-')
		if plus_i == 0:
			for k in range(minus_i):
				pl[k] = '-'
			flips += 1
		for k in range(plus_i):
			pl[k] = '+'
			flag = 1
		if flag:
			flips += 1
			flag = 0
	print('Case #', case, ':', sep='', end = ' ')
	print(flips)