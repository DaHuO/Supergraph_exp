import sys

fin = open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin

T = int(fin.readline())

for t in range(1, T + 1):
	str = fin.readline().rstrip()
	
	out = str[0]
	
	for c in str[1:]:
		if c >= out[0]:
			out = c + out
		else:
			out = out + c
		
	print("Case #{0}: {1}".format(t, out))