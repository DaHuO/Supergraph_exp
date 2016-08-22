a = int(raw_input())

for i in range(a):
	list1 = raw_input().split()
	N = list1[0]
	J = list1[1]
	print('Case #1:')
	for j in range(15):
		for i in range(30-(2*j+1)):
			print('1'+ '0'*(28-2*j-i)+'1'+'0'*2*j +'1'+'0'*i +'1'+' 3 4 5 6 7 8 9 10 11')
	for j in range(1,15):
		for i in range(30-(2*j+1)):
			print('1'+ '0'*(28-2*j-i)+'1'+'0'*(j-1) +'11'+'0'*(j-1) +'1'+'0'*i +'1'+' 3 4 5 6 7 8 9 10 11')
	for i in range(23):
		print('1'+ '0'*(24-i)+'110011'+'0'*i +'1'+' 3 4 5 6 7 8 9 10 11')
	for i in range(23):
		print('1'+ '0'*(24-i)+'111111'+'0'*i +'1'+' 3 4 5 6 7 8 9 10 11')
	for i in range(21):
		print('1'+ '0'*(22-i)+'11111111'+'0'*i +'1'+' 3 4 5 6 7 8 9 10 11')
	for i in range(19-7):
		print('1'+ '0'*(20-i)+'11'*5+'0'*i +'1'+' 3 4 5 6 7 8 9 10 11')
