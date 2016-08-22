filename='output'
target = open(filename, 'w')

def printer(data):
	target.write("Case #%d: %s"%(data[0],data[1]))
	target.write("\n")

def flip(dig):
	if(dig=='-'):
		return '+'
	else:
		return '-'

def test(a):
	count=0
	while not (len(set(a)) <= 1 and list(set(a))[0]=='+'):
		dig=a[0]
		count+=1
		for i in range(0,len(a)):
			if(a[i]==dig):
				a[i]=flip(dig)
			else:
				break
	return count

with open("B-large.in", "r") as ins:
	T=int(ins.readline())

	for i in range(1,T+1):
		digits=[False]*10
		N=(ins.readline())
		N=N.replace("\n", "")
		printer([i,str(test(list(N)))])


