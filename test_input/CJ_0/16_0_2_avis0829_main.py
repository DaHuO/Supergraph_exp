def m1(m,n):
    sum=0
    for i in range(n-1):
        diff=m[i]-m[i+1]
        sum+=max(diff,0)
    return sum

def step(n,s):
    if s==0: return 0
    elif all(n)==1: return 0 # all elements are one
    elif any(n)==0: return 1 # all elements are zero
    elif s==2 and n[0]==0: return 1 
    elif s==2 and n[0]==1: return 2 

    if n[s-1]==1:   return step(n[0:s-1],s-1)
    else:
        for i in range(s):
            n[i] = 0 if n[i]==1 else n[i]==0
            #print("step%i: %d %d" % (s,i,n[i]))
        return step(n[0:s-1],s-1)+1

if __name__ == "__main__":
	tcases = input()

	#print("%s" % (testcases))
	for caseNr in range(1, int(tcases)+1):
		n = [1 if ord(v) == ord('+') else 0 for v in input()]

		maxZ=0
		for i in range(len(n)):
		    if n[i] == 0: maxZ=i

		print("Case #%i: %d" % (caseNr,step(n,maxZ+1)))
