# your code goes here
t = int(input())

for caseno in range(1,t+1):
	t-=1
	seq=input()
	dff=0
	for i in range(1,len(seq)):
		if(seq[i]!=seq[i-1]):
			dff+=1
	if(seq[-1]=='-'):
		dff+=1
	print("Case #%d: %d"%(caseno,dff))