T = input()
for i in range(1,T+1):
	arr = list(raw_input())
	count = 0
	end = len(arr) - 1 
	for j in range (0, end):
		if arr[j] != arr[j+1]:
			count += 1
	
	if arr[end] == "-":
		count += 1

	print "Case #" + str(i) + ": " + str(count)