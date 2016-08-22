def flip(L):
	#print("in flip", L)
	L = L[::-1]
	for i in range(len(L)):
		if L[i]=='-':
			L[i] = '+'
		else:
			L[i] = '-'

	#print("now we have", L)
	return L


for t in range(int(input())):
	inp = list(input())
	count = 0

	while inp.count('+') != len(inp):
		#print(inp)
		if inp[0] == '-':
			try:
				ind = inp.index('+')
			except:
				count+=1
				break

		elif inp[0]=='+':
			ind = inp.index('-')

		inp = flip(inp[:ind]) + inp[ind:]
		#print("now L is ", L)
		count+=1


	print('Case #%d: %d' %(t+1, count))