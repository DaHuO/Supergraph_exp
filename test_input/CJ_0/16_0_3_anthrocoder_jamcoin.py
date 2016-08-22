import sys
import math

def test_jamcoin(jam_test):
	jams = []
	for i in range (2, 11):
		curjam = int(jam_test, i)
		#print("currently testing: " +str(curjam))
		if curjam == 2 or curjam <= 1:
			return []
		if curjam % 2 == 0:
		#	print ("2 is a divisor")
			jams.append(int(curjam/2))
			continue

		sqr = int(math.sqrt(curjam)) + 1
		found = False

		for divisor in range(3, sqr, 2):
			if curjam % divisor == 0:
				jams.append(divisor)
		#		print (str(divisor) + " is a divisor")
				found = True
				break
		if not found:
			return []
	return jams

try: 
	f = open(sys.argv[1])
	out = open(sys.argv[1].rpartition("\\")[2]+".out", 'w')

	numTests = int(f.readline())
	jamcoins = []

	for i in range (0, numTests):
		vals = f.readline()[0:-1].split(" ")
		N = int(vals[0])
		J = int(vals[1])
		out.write("Case #" + str(i+1) +": \n")
		jam_test = '1' + ('0'*(N-2)) + '1'
		for k in range(0, J):			
			divisors = test_jamcoin(jam_test)
			while jam_test in jamcoins or len(divisors) == 0:
				jam_test = str(bin(int(jam_test,2) + 2)[2:])
		#		print("current jam test: " + jam_test)
				if len(jam_test) > N: 
					break
				divisors = test_jamcoin(jam_test)
			jamcoins.append(jam_test)
			out.write(str(jam_test) + " ")
			for m in range(0, len(divisors)):
				out.write(str(divisors[m]) + " ")
			out.write("\n")
		

except IOError as e:
	print ('Error:', err) 




