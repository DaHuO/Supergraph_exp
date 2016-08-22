import numpy
import random
def isprime(number):
    ''' if number != 1 '''
    if (number > 1):
        ''' repeat the test few times '''
        for time in xrange(3):
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            randomNumber = random.randint(2, number)-1
            
            ''' Test if a^(n-1) = 1 mod n '''
            if ( pow(randomNumber, number-1, number) != 1 ):
                return False
        
        return True
    else:
        ''' case number == 1 '''
        return False 

def smallestdivisor(n):
	"""returns the smallest non-trivial divisor of n"""
	d = 2 # to begin
	while n % d != 0:
		d = d+1
	return d


f = open('C-small-attempt0.in')
count = int(f.readline())
for j in range(1,count+1):
	print ('CASE #'+str(j)+': ')
	string = f.readline().rstrip()
	numbers = string.split()
	N = int(numbers[0])
	J = int(numbers[1])
	final = []
	K = N-2
	keep_running = True
	while keep_running:
		arr = numpy.random.randint(2, size=(K,))
		candidate = str(1)+(''.join(str(x) for x in arr))+str(1)
		found = True
		for m in range(10,1,-1):
			if isprime(int(candidate,m)):
				#print(str(int(candidate,m)) + ' is prime')
				found = False
		if candidate in final:
			found = false
		if found:
			final.append(candidate)
			answer = str(candidate)
			for n in range(2,11):
				divisor = smallestdivisor(int(candidate,n))
				answer = answer + ' ' + str(divisor)
			print answer
		if J == len(final):
			break
	

			
f.close()