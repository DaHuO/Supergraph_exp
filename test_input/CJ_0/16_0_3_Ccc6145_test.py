def coinJam(num):
	ret = []
	for i in xrange(2, 11):
		j = int(num, i)
		for k in xrange(2, min(int(j**0.5), 10000)):
			if j % k == 0:
				ret += str(k),
				break
		if len(ret) < i - 1:
			return False
	return ret

def getNext(s):
	a = [int(i) for i in s][::-1]
	a[0] += 1
	i = 0 
	while a[i] > 1:
		a[i+1] += 1
		a[i] = 0 
		i += 1
	a[0] = 1

	return ''.join([str(j) for j in a[::-1]])

print 'Case #1:'
 
t = int(raw_input())
n, j = [int(i) for i in raw_input().split()]

num = '1'+'0'*(n-2)+'1'

while j > 0:

	# print num
	ret = coinJam(num)
	if ret:
		j -= 1
		print num + ' ' + ' '.join(ret)
	num = getNext(num)





