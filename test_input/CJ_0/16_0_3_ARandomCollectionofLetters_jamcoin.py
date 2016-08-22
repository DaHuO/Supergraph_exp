import numpy as np
#raw_input()
#raw_input()

i=500
io=i
n=32
ulim=1000
flag=0
arr=[None]*i
while True:
	flag=0
	val=2**(n-1)+2*np.random.randint(2**(n-2))+1
	str_rep=np.binary_repr(val)
	jv=[None] *10
	jv[0]=int(str_rep)
	for b in range(2,11):
		num=int(str_rep,b)
		# Now we need to check if num is prime	
		for v in range(3,ulim,2):
			if (num%v==0):
				jv[b-1]=v
				break

		if jv[b-1] is None:
			flag=1
			break
	if (flag==1):
		continue
	else:
		i=i-1
		arr[i]=jv
	if i<0:
		break
print "Case #1:"
for i in range(io):
	print arr[i][0],arr[i][1],arr[i][2],arr[i][3],arr[i][4],arr[i][5],arr[i][6],arr[i][7],arr[i][8],arr[i][9]

#Verify correct output with: python jamcoin.py > output.txt; tail -n +2 output.txt | awk '{print $1}' | sort | uniq | wc -l
