x = int(input())
for i in range(x):
	dic = {"+" : "-" , "-" : "+"}
	s = input()
	x = list(s)
	res = 0
	while True:
		y = x[0]
		aux = 0
		b = False
		c = False
		while aux < len(x) and x[aux] == y:
			if x.count('+') == 0:
				b = True
			else:
				c = True
			x[aux] = dic[y]
			aux = aux + 1
			if x.count('-') == 0:
				aux = len(x)
				if b:
					res = res + 1
				elif c:
					res = res + 1
		if aux == len(x):
			print("Case #"+ str(i + 1) + ": " + str(res))
			break
		res = res + 1
			
