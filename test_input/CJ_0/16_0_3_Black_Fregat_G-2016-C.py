t, = map(int, input().split())
for tt in range(t):
	print("Case #{0}:".format(tt+1))
	n, j = map(int, input().split())
	start = 1 << int(n/2-1)
	for jj in range(j):
	  left = "{0:b}".format(start+jj)
	  print(left+left[::-1], "3 2 5 2 7 2 3 2 11")
