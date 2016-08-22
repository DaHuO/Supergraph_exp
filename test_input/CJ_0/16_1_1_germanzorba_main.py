
def rearrange(W,S):
	S=W[0];
	for i in range(1,len(W)) :
		if S[0] > W[i]: S = S + W[i]
		else : S = W[i] + S 
	return S

T = int(raw_input())
for t in range(1,T+1):
	W = raw_input()	
	print "Case #{}: {}".format(t, rearrange(W,"") )
