from math import sqrt
from itertools import count, islice

def factorGen(n):
    if n < 2: 
    	return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return number
    return False

def main(l,no):
	d = {}
	i = int("1"*(l-2), 2)
	while len(d) < no:
		curNo = "{0:b}".format(i) + "1"
		if len(curNo) < l:
			i += 1
			continue
		if len(curNo) > l:
			return d
		primeData = checkPrimes(curNo)
		if primeData['valid']:
			d[curNo] = primeData['factors']
		i += 1
	return d

def formatter(d):
	returnString = "\n"
	for number in d:
#		print "No of divisors: " + str(len(d[number]))
		returnString += number + " " + " ".join([str(i) for i in d[number]]) + "\n"
#	print "Dictionary of: " + str(len(d))
	return returnString[:-1]

def checkPrimes(num):
	results = {'valid':False,'factors':[]}
	bases = [2,3,4,5,6,7,8,9,10]
	for base in bases: 
		numConverted = int(num,base)
		factor = factorGen(numConverted)
		if factor == False:
			results['valid'] = False
			break
		if factor != numConverted and factor != 1:
			results['factors'] += [factor]
			results['valid'] = True
			continue
		results['valid'] = False
	return results


def fileHandler(inName):
	returnString = ""
	f = open(inName,'r')
	i = 1
	init = True
	for line in f:
		if init == True:
			init = False
			continue
		returnString += "Case #" + str(i) + ": " + formatter(main(int(line.split()[0]),int(line.split()[1]))) + "\n"
		i += 1
	f.close()
	w = open('results.txt','w')
	w.write(returnString)
	w.close()

fileHandler("C-small-attempt0.in")