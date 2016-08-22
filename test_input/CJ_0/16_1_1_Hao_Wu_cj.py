

def a():
	f = open("A-large.in")
	T = int(f.readline())	
	ct = 0
	while (T>0):
		T-=1
		ct+=1
		s = f.readline()[:-1]
		cur = ""
		for t in s:
			cur1 = t + cur
			cur2 = cur + t
			if cur1 > cur2:
				cur = cur1
			else:
				cur = cur2
		print "Case #"+str(ct)+": " + cur
	f.close()


if __name__ == "__main__":
	a()