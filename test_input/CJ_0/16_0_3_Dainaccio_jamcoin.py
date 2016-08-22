import os, random

def rev(s):
	
	"{0:08b}".format(my_int)
	return tmp
	
def random_coin(n):
	
	tmp = ''.join(random.SystemRandom().choice("10") for _ in range(n-2))
	
	return "1" + tmp + "1"
	
def check_coin(coin):
	
	for base in range(2,10+1):
		check_div(int(coin,base))

	return True
	
def check_div(n):
	
	#for i in range(3,n):
	for i in range(3,999):
		if float(n)/i == float(n)//i:
			return i
	
	
	return 0
	
	


if __name__ == '__main__':

	file = open('IN', 'r')
	dati = file.read().split('\n')
	
	T = int(dati[0])
	
	#dati = dati[1:-1]
	dati = dati[1].split()
	
	N = int(dati[0])
	J = int(dati[1])
	
	
	for i in range(T):
			
		print "Case #%i:"%((i+1))
		
		j = 0
		coins = []
		while j < J:
		
			coin = random_coin(N)
			while coin in coins:
				coin = random_coin(N)
			
			divs = []
		
			for base in range(2,10+1):
				div = check_div(int(coin,base))
			
				if div == 0:
					break
				else:
					divs.append(div)
		
			if len(divs) == 9:
				# ok
				j = j + 1
				coins.append(coin)
				print coin, 
				for d in divs:
					print d,
				print

		
		
		
		
		
