input()
dat=input().split()
length=int(dat[0])
count=int(dat[1])

for i in range(2**(length-2)):
	jamcoin=bin(i)[2:]
	while len(jamcoin)<length-2:
		jamcoin='0'+jamcoin
	jamcoin='1'+jamcoin+'1'
	
	prime=True
	output=jamcoin
	for b in range(2,11):
		v=int(jamcoin,b)
		i=2
		prime=True
		while i*i<=v:
			if v%i==0:
				prime=False
				output+=' '+str(i)
				break
			i+=1
		if prime:
			break
	if not(prime):
		print(output)
	