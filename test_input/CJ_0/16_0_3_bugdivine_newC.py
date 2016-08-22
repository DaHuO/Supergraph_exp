import itertools, math

def solution(s):
#	print s
	flag = 0
	ps = [s]
	for x in range(2, 11):
		num = int(s, base=x)
		prime = 0
		y = 3
		no = int(math.sqrt(num))
		while(y < no+1 and y<10000000):
			if num%y==0:
				ps.append(str(y))
				prime = 1
				break
			y+=2
		if (prime == 0):
			flag = 1
			return []
	return ps

def ops(num, l):
	if l==0:
		return []
	if num>=l:
		return ['1'*l]
	if num == 0:
		return ['0'*l]
	s = ''
	ans = []
	a=0
	for b in ops(num-1, l-1):
		s = '1'
		s += b
		ans.append(s)
	for b in ops(num, l-1):
		s = '0'
		s += b
		ans.append(s)
	return ans


t = int(raw_input())
case = 0
while t>0:
	t-=1
	case+=1
	print "Case #"+str(case)+":",
	counted = []
	n, j = map(int, raw_input().split())
	for a in itertools.product(['0', '1'], repeat=n-2):
		s = '1'+''.join(a)+'1'
		if counted.count(s)>0:
			continue
#		print s
		flag = 0
		ps = []
		for x in range(2, 11):
			num = int(s, base=x)
			prime = 0
			y = 3
			no = int(math.sqrt(num))
			while(y < no+1):
				if num%y==0:
#					ps.append(str(y))
					prime = 1
					break
				y+=2
			if (prime == 0):
				flag = 1
				break
		if flag == 0:
			count = s.count('1')-2
			arr = ops(count, n-2)
#			print "Count", count, arr, s, counted
			for xubu in arr:
				Sop = '1'+xubu+'1'
#						print Sop
				counted.append(Sop)
#						print solution(Sop), " SOP"
				an = solution(Sop)
				if len(an)>1:
					j-=1
					print ' '.join(an)
					if j==0:
						break
#			for a in ps:
#				print ' '.join(a)
#			print '\n'.join(ps)
		if j==0:
			break