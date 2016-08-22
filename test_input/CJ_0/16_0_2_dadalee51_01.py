import fileinput
import collections

def join(arr):
	outStr=""
	for i in arr:
		outStr= outStr + str(i) + " "
	return outStr.strip()


def solve(fileName):
	ans=0
	fout = open(fileName+".pythout", 'w')
	with open(fileName, 'r') as f:
		T = int(f.readline())
		for ci in range(T):
			print "----------case ",ci+1
			m = f.readline()
			print "read:"+m
			n=m[::-1].strip()
			print "orig:"+n
			p=n[0]
			for i in range(len(n)-1) :
				if n[i]!=n[i+1] :
					p=p+str(n[i+1])
			print "p is:"+p
			if p[0]=="+":
				p = p[1:]
			print "new p:" + p
			ans = len(p)
			print "ans:" , ans
			fout.write("Case #"+str(ci+1)+": " +str(ans)+ "\n")	
	return;

#solve here.
#solve("test")
solve("small")
#solve("large")