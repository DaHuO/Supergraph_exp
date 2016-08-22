T = input()
for t in range(1,T+1):
	arr = list(raw_input())
	ans = []
	ans.append(arr[0])

	for i in range(1,len(arr)):
		if arr[i]>=ans[0]:
			ans.insert(0, arr[i])
		else:
			ans.append(arr[i])

	print "Case #" + str(t) + ": " + ''.join(str(x) for x in ans)