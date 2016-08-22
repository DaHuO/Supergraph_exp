import copy;
T=input();
ans=[];

for i in range(T):

	s=raw_input();
	l=[];
	l.append(s[0]);
	for i in range(1,len(s)):
		l1=copy.deepcopy(l);
		l2=copy.deepcopy(l);
		l1.append(s[i]);
		l2.insert(0,s[i]);
		if(cmp(l1,l2)>0):
			
			l=l1;
			#print(l);
		else:
			
			l=l2;
			#print(l);
	ans.append(l);
for i in range(T):
	print("Case #"+str(i+1)+": "+''.join(ans[i]));
