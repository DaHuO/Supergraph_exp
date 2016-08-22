def list_rindex(l, v):
	try:
		return len(l) -1 - l[::-1].index(v)
	except ValueError:
		raise

def get_flips(S):
	i = 0
	while True:
		try:
			n = list_rindex(S,0)
			S[:n+1] = [0 if i == 1 else 1 for i in S[:n+1]]
			i+=1
		except ValueError:
			break
	return i


T = int(input())
for i in range(1,T+1):
	S = input()
	S = [0 if i == '-' else 1 for i in S]
	print("Case #{}: {}".format(i, get_flips(S)))
	
