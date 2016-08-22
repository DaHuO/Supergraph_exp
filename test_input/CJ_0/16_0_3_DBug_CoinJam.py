def check_prime(n):
	#print "Is_Prime",n
	for i in range(2,1000):
		if(n%i==0):
			return i
	return 0

fp1 = open("input.in",'r')
t = int(fp1.readline())
n,j = map(int,fp1.readline().strip().split(" "))
fp = open("output.txt",'w')
num1 = 32769
turn=0
fp.write("Case #1:\n")
for i in range(130):
	num = bin(num1)[2:]
	#print "num",num
	fact = []
	ans = num
	for i in range(2,11):
		#print "Chacking base",i
		factr = check_prime(int(num,i))
		#print "factr",factr
		if factr!=0:
			fact.append(factr)
			ans+=" "+str(factr)
	if(len(fact)==9):
		if(turn==0):
			fp.write(ans)
		else:
			fp.write("\n"+ans)
		turn+=1
	num1+=2