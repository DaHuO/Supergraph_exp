import math
def Dividi(x):
	d=1
	for i in range(2, int(math.sqrt(x))+1):
		if x%i == 0: return i
	return d
N=32
J=500
c=0
for i in range(2**(N-1) + 1, 2**N, 24):
	#print("Guardo %s" % ("{0:b}".format(i)))
	s=str("{0:b}".format(i))
	if s.count('1') % 2 == 1: 
		continue
	for b in range(2, 11):
		t = int("{0:b}".format(i), b)
		#print("\tBase %s: %s" %(b, t))
		d=1
		if b%2==1: d=2
		else: d=Dividi(t)
			
		if d>1:
			s+= " " + str(d)
		else:
			s=""
			break
		

	if len(s)>0:
		print(s)
		c+=1
	if c==J:
		break

print(c)
