factors = [-1,-1, -1,-1,-1,-1,-1,-1,-1,-1,-1]



def valueof(x, b):
	ret = 0;
	
	for v in x:
		ret = ret*b
		if(v=='1'):
			ret += 1

	return ret
	
def isPrime(n):
    if n==2 or n==3: return -1
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return i    

    return -1

def main():
	t = int(input()) 
	n, j = [int(s) for s in input().split(" ")] 
	guess = 1 << (n-1)
	guess += 1


	limit = 1<<n
	count = 0
	while(guess < limit and count < j):
		binstring = str(bin(guess));
		guesstring = binstring[2:len(binstring)];
		flag = True			
		for i in range(2,11):
			v = valueof(guesstring,i)
			#print(v);

			factors[i] = isPrime(v)
			#print(factors[i]);
			if(factors[i]<0):
				flag = False
				break

		if(flag): 
			count += 1
			print("{} {} {} {} {} {} {} {} {} {}".format((guesstring), factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10]))
		guess += 2;
	return



print("Case #1:")

main()