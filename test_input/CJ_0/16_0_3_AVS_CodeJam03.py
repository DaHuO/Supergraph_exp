def ibs(s):
	return '{:032b}'.format(1 + int(s, 2))

x=''

def create(n):
	global x
	temp="1"
	for i in range(n-2):
		temp+='0'
	temp+='1'
	x=temp

def isPrime(num):
	if num < 2:
		return False
	if num == 2:
		return True
	else:
		for div in [2,3,5,7,11]:
			if num % div == 0:
				return False
		return True

def basen(d,n):
	flag=0
	a=int(d,base=n)
	for i in [2,3,5,7,11]:
		if(a%i==0):
			flag=i
			break
	if(flag==0):
		return False
	else:
		return flag	

def check(n):
	flag=0
	xb=[]
	xb.append(int(n,base=2))
	xb.append(int(n,base=3))
	xb.append(int(n,base=4))
	xb.append(int(n,base=5))
	xb.append(int(n,base=6))
	xb.append(int(n,base=7))
	xb.append(int(n,base=8))
	xb.append(int(n,base=9))
	xb.append(int(n,base=10))
	for i in xb:
		if(isPrime(i)):
			flag=1
			break
	if flag==0:
		return True
	else:
		return False

def coinJam(case,n,j):
	c=0
	create(n)
	global x
	print ("case #{0}:".format(case))
	while c<j:
		#if(check(x)):
			if(basen(x,2)and basen(x,3)and basen(x,4)and basen(x,5)and basen(x,6)and basen(x,7)and basen(x,8)and basen(x,9)and basen(x,10)):
				li_1=[]
				li_1.append(x)
				li_1.append(basen(x,2))
				li_1.append(basen(x,3))
				li_1.append(basen(x,4))
				li_1.append(basen(x,5))
				li_1.append(basen(x,6))
				li_1.append(basen(x,7))
				li_1.append(basen(x,8))
				li_1.append(basen(x,9))
				li_1.append(basen(x,10))
				for i in li_1:
					print(i,end=' ')
				print('')
				c+=1
				x=ibs(x)
				x=ibs(x)
			else:
				x=ibs(x)
				x=ibs(x)
		#else:
		#	x=ibs(x)
		#	x=ibs(x)


T=int(input())
for i in range(T):
	n=str(input())
	n=n.split()
for i in range(T):
	coinJam(i+1,int(n[0]),int(n[1]))
