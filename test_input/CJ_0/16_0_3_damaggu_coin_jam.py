# Coin Jam
# Markus Marks 

import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap

@timing
def factorization(N):

   factors = []
   # for i in range(2,N):
   i=2
   while(i<100):
   	if(N%i==0):
   		if not factors:
   			factors.append(i)
   		else:
   			he=1
   			for factor in factors:
	   			if(i%factor==0):
	   				he=0
	   		if(he==1):
	   			factors.append(i)
	i = i + 1
   return factors

@timing
def factorization_string(N_string,base):

   factors = []
   N = int(N_string, base)
   # for i in range(2,N):
   i=2 

   while(i<100):

   	su = 0
   	for u in range(len(N_string)-1, -1, -1):
   		exp = int(N_string[u])
   		new = (base ** (exp%i)) % i
   		su = su + new

   	if(su%i==0):
   		if not factors:
   			factors.append(i)
   	i = i + 1
   return factors


@timing
def checkNotPrime(N_string):

	ret = 1
	factorBase = []

	for i in range(2,11):
		N = int(N_string, i)
		factors = factorization(N)
		# factors = factorization(N_string,i)
		if not factors:
			ret = 0
			break
		factorBase.append(factors[0])

	return (ret,factorBase)

@timing
def createJamcoins(N,J):

	jamcoins = []
	divs = []

	if(N>2):
		length = int(N)-2
		middle_n = 0

		while(len(jamcoins) < int(J)):

			
			middle = bin(middle_n).split('b')[1]
			diff = length -len(middle)
			if(diff > 0):
				middle = '0' * diff + middle
			jamcoin = '1' + middle + '1'

			ret, factors = checkNotPrime(jamcoin)
			if ret:
				jamcoins.append(jamcoin)
				f_out.write(jamcoin)
				f_out.write(' ')
				f_out.write(" ".join(str(factor) for factor in factors))
				f_out.write('\n')

			middle_n = middle_n + 1

	return jamcoins, divs



f = open('input.txt')
f_out = open('output.txt', 'w')
inp = f.read().split('\n')
f.close()
he = inp[1].split(' ')
f_out.write('Case #1:\n')


N = he[0]
J = he[1]

coins, divs = createJamcoins(N,J)


f_out.close()