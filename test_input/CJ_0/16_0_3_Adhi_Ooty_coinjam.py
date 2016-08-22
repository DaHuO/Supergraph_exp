from random import randint
from math import pow, sqrt


T = 1
N = 16
J = 50
count = 0
jamCoins = [0]
file = open("output.txt", "w")
file.write("Case #1: \n")

def primeTest(number):
	flag = 0
	if (number==2 or number == 3):
			flag = 0
	else:
		for k in range(2, int(sqrt(number))+1):
			if(number%k == 0):
				flag = k
				break
		return flag

while(count<J):	
	jamCoin = [1]	
	for i in range(N-2):
		jamCoin.append(randint(0,1))
	jamCoin.append(1)

	valid = 1	

	bases = []

	for i in range(2, 11):
		number = 0	
		for j in range(N):
			number = number + jamCoin[N-1-j]*pow(i, j)
		bases.append(number)
		
	if bases[8] in jamCoins:
		continue
		
	div = []
	
	for i in range(9):
		d = primeTest(bases[i])
		if d==0:
			valid = 0
			break
		else:
		    div.append(d)
		
		
	if valid == 1:
 		file.writelines("".join(str(i) for i in jamCoin) + " "+ " ".join(str(i) for i in div) + "\n")
 		count=count+1
 		jamCoins.append(bases[8])
		
file.close()


