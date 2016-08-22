
def isPrime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True
  

smallPrimes = [i for i in range(100000) if isPrime(i)]

def mightBePrime(n):

	i = 0
	r = int(n ** 0.5)

	while i < len(smallPrimes) and smallPrimes[i] <= r:
		p = smallPrimes[i]
		if n % p == 0:
			return str(p) , False
		i += 1

	return "0" , True

def convertToBase(coin, base):
	return sum([int(coin[::-1][j])*(base**j) for j in range(len(coin))])

def testCoin(coin):

	valid = True
	divisors = []
	for base in range(2,11):
		v = convertToBase(coin, base)
		d , mbp = mightBePrime(v)
		divisors.append(d)
		if mbp:
			valid = False
			break

	if valid:
		return coin + " " + " ".join(divisors)
	else:
		return ""

def generate(n, j):

	i = 0
	results = []

	while i < 2**(n-2) and len(results) < j:

		coin = "1" + ('{0:0' + str(n-2) + 'b}').format(i) + "1"

		result = testCoin(coin)

		if result:
			results.append(result)
			
		i += 1

	return results


name = "C-large"
n = 32
j = 500

results = generate(n, j)

out = open(name + ".out",mode='w')
out.write("Case #1:" + "\n")

for line in results:
	out.write(line + "\n")
out.close()
