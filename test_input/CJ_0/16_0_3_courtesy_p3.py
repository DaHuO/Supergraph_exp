p = [[0 for x in range(32)] for x in range(11)] 

for i in range(2,11):
	p[i][0] = 1
	for j in range(1,32):
		p[i][j] = p[i][j-1]*i


SZ = 1000000

pm = []

f = [0]*SZ
for i in range(2,SZ):
	if f[i] == 0:
		pm.append(i)
		for j in range(i,SZ,i):
			f[j] = 1


def check(t):
	for i in pm:
		if i>=t:
			return -1
		if t%i == 0:
			return i
	return -1

k = 0
J = 500
N = 32


print "Case #1: "


i = 0
while k<J:
	a = [0]*11
	for j in range(2,11):
		a[j] += p[j][N-1] + 1
	t = i
	i+=1
	j = 1
	while t>0:
		if t%2==1:
			for t1 in range(2,11):
				a[t1] += p[t1][j]
		j+=1
		t/=2
	b = [0]*11
	fl = 1
	for j in range(2,11):
		b[j] = check(a[j])
		if b[j]<0:
			fl = 0
			break
	if fl == 1:
		x = "{0:b}".format(a[2])
		print x,
		for j in range(2,11):
			print b[j],
		print ""
		k+=1
