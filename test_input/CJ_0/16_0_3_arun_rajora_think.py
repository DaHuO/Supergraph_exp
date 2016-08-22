al= 10000001
limit= 10000
def isprime(x):
	j=3
	while(j*j<=x and j<=limit):
		if(x%j==0):
			return j
		j+=2
	return 0;
def disp_bin(x):
	if(x>0):
		disp_bin(int(x/2))
		print(x%2,end="")

def sol(x):
	arr=[0,0,0,0,0,0,0,0,0,0]
	i=2
	while(i<=10):

		bx=0
		mul=1
		temp=x
		while(temp!=0):
			if(temp%2==1):
				bx+=mul
			temp/=2
			temp=int(temp)
			mul*=i
		arr[i-1]=isprime(bx)
		if(arr[i-1]==0):
			return -1

		i=i+1
	disp_bin(x)
	i=2
	while(i<=10):
		print("",arr[i-1],end="")
		i=i+1
	print("")
	return 0
def main():
		print("Case #1:")
		n=32
		j=500
		start=(1)<<(n-1)
		while(j>0):
		
			if(start%2==0):
			
				start+=1
				continue
			if(sol(start)!=-1):
				j-=1
				
			start+=1
			
		

main()