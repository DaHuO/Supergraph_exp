'''input
5
-
-+
+-
+++
--+-
'''
for T in range(int(input())):
	S = [0 if x == '-' else 1 for x in input()]

	flips = 0
	for i in reversed(range(len(S))):
		if S[i] == 0:
			if S[0] == 1:
				j = S.index(0)
				S = [0 if x else 1 for x in reversed(S[:j])] + S[j:]
				flips += 1

			j = i+1
			S = [0 if x else 1 for x in reversed(S[:j])] + S[j:]
			flips += 1

	print("Case #{}: {}".format(T+1, flips))