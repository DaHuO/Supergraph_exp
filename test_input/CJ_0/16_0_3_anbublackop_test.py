
all_jams=set()

def Divisor(n):
    if n%2==0:
    	ans=2
    else:
    	for i in range(3,int(n**0.5)+2,2):
    		if n%i==0:
    			ans=i
    			break
    return ans				

    
def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True



def printlength(s,k):
	n=len(s)
	printalllengthrec(s,"",n,k)

def printalllengthrec(s,prefix,n,k):
	if k==0:
		all_jams.add('1'+prefix+'1')
		return
	
	for i in range(n):
		newprefix=prefix+s[i]
		printalllengthrec(s,newprefix,n,k-1)

from collections import defaultdict as dfdt

for _ in range(int(input())):		
	N,J=map(int,input().split())
	printlength('01',N-2)

	all_jams_list=list(all_jams)

	final2=dfdt(list)
	length=len(all_jams_list)

	for i in range(length):
		s=list()
		for k in range(2,11):
			base=int(all_jams_list[i],k)
			if not isprime(base):
				d=Divisor(base)
				s.append(d)	
				if len(s)==9:
					break			
			else:
				break
		if len(s)==9:
			final2[all_jams_list[i]].append(s)		
		if len(final2)==J:
			break		
	print ("Case #{}: ".format(_+1))
	for keys in final2.keys():
		print (keys,*list(*final2[keys]))
				





		
			
