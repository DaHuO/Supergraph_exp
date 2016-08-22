T=1
N=32
J=500
count=0;

for temp in range(1,T+1):
	print('Case #' + str(temp) + ': ')
	
	num=(2**(N-1))+1
	while num < 2**N and count < J:
		numbase = [0] * 11
		check = [0]*11 
		factors = [0]*11
		flag=1
		#print num
		for base in range(2,11):
			for j in range(N): #change
				if(num & (2**j)):
					numbase[base]+=base**j;

			#Primality testing
			for i in range(2, int(numbase[base]**(0.1))+1): #change
				if (numbase[base]%i) == 0:
					factors[base]=i
					check[base]=1
					break
			if check[base] == 0:
				flag=0
				break
			
		if(flag):
			count+=1
			#printf("%d ",num);
			#vector<int> num2;
			#for(int ii=num;ii>0;ii/=2)
		#		num2.push_back(ii%2);
			#for(int ii=num2.size()-1; ii>=0; ii--)
		#	for ii in range(num2.size()-1, 0, -1):
			
			print(numbase[10]),
			for base in range(2,11):
				print(factors[base]),
				#printf(" %d: %lld; ",base, numbase[base]);
			print('')
		num += 2