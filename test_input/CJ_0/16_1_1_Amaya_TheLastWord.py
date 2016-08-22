T = input();
tempT = T;
result = [];
while(T!=0):
	s = raw_input();
	word = s[0];
	end = len(s);
	for i in range(1,end):
		if(s[i] >= word[0]):
			word = s[i]+word[0:];
		else:
			word = word[:len(word)] + s[i];
	result.append(word);
	T=T-1

i=0
while(i<tempT):   
    print "case #"+str(i+1)+":",result[i]
    i = i+1