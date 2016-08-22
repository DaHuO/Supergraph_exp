import sys 
sys.stdin.readline()

kase = 0
for l in sys.stdin:

	kase+=1
	head = l[0]
	ans = l[0]
	for i in range(1,len(l)-1):
		if l[i] >= head:
			ans = l[i] + ans
			head = l[i]
		else:
			ans += l[i] 

	print("Case #" + str(kase) +": " + ans)

