import sys
n = 32
j = 500
done = 0
def baseconversion(x, base):
	global n
	sum = 0
	for i in range(0,n):
		# print i
		sum = sum+(int(x[i])*(base**(n-1-i)))
	return sum

def next(p) :
	global n
	q = "1"
	for i in xrange(n-2,0,-1):
		if p[i] == '0':
			q = "1"+q
			q = p[:i]+q
			return q
		else:
			q = "0"+q

def fsd(z):
	divisor = z
	for x in xrange(2,int(z**0.5)+1,1):
		# print int(z**0.5)+1
		if x > 1000000:
			break
		if z%x == 0:
			divisor = x
			# print "here"+str(x)
			break
	return divisor

print "Case #1:"
start = "1"+"0"*(n-2) + "1"
# print fsd(1000)

while (done!=j):
	# print start
	isjam = True
	temp = []
	for base in range(2,11):
		mynum = baseconversion(start,base)
		# print mynum
		fsdivisor = fsd(mynum)
		# print fsdivisor
		if fsdivisor == mynum :
			isjam = False
			break
		temp.append(fsdivisor)
	if isjam :
		sys.stdout.write(start+" ")
		for x in range(0,9):
			sys.stdout.write(str(temp[x]) + " ")
		done = done+1
		print ""
	start = next(start)