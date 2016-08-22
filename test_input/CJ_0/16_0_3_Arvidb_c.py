'''input
1
6 3
'''
for T in range(int(input())):
	N, J = map(int, input().split())
	
	print("Case #{}:".format(T+1))

	k = 0
	for j in range(J):
		divs = []
		val = None
		while len(divs) != 9:
			divs = []
			for base in range(2, 11):
				val = '1{0:0{1}b}1'.format(k, N-2)
				res = int(val, base)

				for d in [2, 3, 5, 7, 11, 13, 17]:
					if res % d == 0:
						divs.append(str(d))
						break
			k += 1


		print(val, " ".join(divs))