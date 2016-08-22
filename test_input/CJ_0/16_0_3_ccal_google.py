import itertools

def obtenerBases(nCoin):
	divisores = []
	for base in range(2,10+1):
		number = int(nCoin,base)
		if is_prime(number,divisores):
			return False
	print nCoin, 
	for divisor in divisores:
		print divisor,
	print
	return True

def is_prime(n, divisores):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: 
	divisores.append(2)
	return False
  if n < 9: return True
  if n%3 == 0: 
	divisores.append(3)
	return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: 
	divisores.append(f)
	return False
    if n%(f+2) == 0: 
	divisores.append(f+2)
	return False
    f +=6
  return True    

print 'Case #1:'
N = 16
J = 50
i=0
for seq in itertools.product("01", repeat=N-2):
	coin = '1'
	for ch in seq:
		coin += ch
	coin += '1'
	if(obtenerBases(coin)):
		i+=1
	if i>J:
		break	
	
