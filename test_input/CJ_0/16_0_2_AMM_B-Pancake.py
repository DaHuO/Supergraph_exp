def least_number_of_flips(sequence):
	print sequence
	if len(sequence)==0:
		return 0
	else:
		sequence=remove_tail(sequence,sequence[-1])
		return 1+least_number_of_flips(sequence)


def remove_tail(sequence,symbol):
	i=1
	while(i<=len(sequence) and sequence[-i]==symbol):
		i+=1
	return sequence[:(-i+1)]

f=open("B-large.in","r")
g=open("write_B_large.out","w")
content=f.read()
content=content.split()
T=int(content[0])

for t in xrange(1,T+1):
	sequence=content[t]
	bias={'+':1,'-':0}
	g.write("Case #"+str(t)+": " + str(least_number_of_flips(sequence)-bias[sequence[-1]])+"\n")