from __future__ import print_function
import fileinput
from sets import Set

def flip(N, last):
	for i in range(len(N)):
		if i == last+1:
			break
		else:
			if N[i] == "-":
				N[i] = "+"
			else:
				N[i] = "-"
	return N

def all_plus(N):
	for c in N:
		if c == "-":
			return False
	return True

f = fileinput.input()

T = int(f.readline())
for case in range(1,T+1):
	N=list(f.readline().rstrip())
	count = 0
	while not all_plus(N):
		for i in range(1,len(N)+1):
			if N[-i] == "-":
				count += 1
				N=flip(N, len(N)-i)
				break
	print("Case #"+str(case)+": "+str(count))
