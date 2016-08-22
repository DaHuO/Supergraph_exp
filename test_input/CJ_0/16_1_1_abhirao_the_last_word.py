T = int(input())
for t in range(T):
	s = input()
	b = list(set(s[:]))
	b.sort()	
	# print(b)
	a = [s[0],]
	for c in s[1:]:
		i = b.index(c)
		# print(i, b.index(a[0]), a)
		if(i >= b.index(a[0])):
			a = [c] + a
		else:
			a = a + [c]
	print("Case #"+str(t+1)+": "+(''.join(a)))