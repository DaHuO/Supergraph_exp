from itertools import groupby

T = int(raw_input())

for case in range(T):
    S = raw_input()

    answer = [S[0],]
    for c in S[1:]:
	 	if c <= answer[-1]:
	 		answer.append(c)
	 	elif c > answer[-1] and c < answer[0]:
	 		answer.append(c)
	 	else:
	 		answer.insert(0, c)

    print "Case #%d: %s" % (case+1, "".join(answer))