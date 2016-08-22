T = input();
tempT = T;
result = [];
while(T!=0):
	n = raw_input();
	k = len(n) * '+';
	turn = 0;
	while(n != k):
		i = 0;		
		while(i != len(n)-1 and n[i] == n[i+1]):
			i=i+1;
		temp = n[:i+1];
		temp = temp[::-1];
		for j in range(0,i+1):			
			if(temp[j] == '+'):
				n = n[:j]+'-'+n[j+1:];
			if(temp[j] == '-'):
				n = n[:j]+'+'+n[j+1:];
		turn = turn +1;
	result.append(turn);
	T=T-1

i=0
while(i<tempT):   
    print "case #"+str(i+1)+":",result[i]
    i = i+1