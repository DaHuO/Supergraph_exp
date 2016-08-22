import math

def problem3():

	print "Case #1:"

	N = 32
	J = 500

	base = (1 << (N-1)) |  1
	numFound = 0

	for i in range(2,2**(N-1),2):
		temp = base | i
		factors = [0]*9
		comp = True
		for j in range(2,11):
			factors[j-2] = findFactor(baseChange(temp,j))
			if factors[j-2] == 0:
				comp = False
				break
		if comp:
			s = ''
			for i in factors:
				s += ' ' + str(i)
			print str(baseChange(temp,10)) + s
			numFound += 1
			if numFound == J:
				break

	if numFound != J:
		print "DO NOT USE! Not Enough Found. Increase factor size"





def findFactor(num):
	top = 30
	for i in range(3,top,2):
		if num % i == 0:
			return i
	return 0


def baseChange(num,base):
	i = 0
	temp = 0
	while num > 0:
		temp += (num & 1) * (base ** i)
		i += 1
		num = num >> 1
	return temp


problem3()