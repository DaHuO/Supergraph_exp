#!/bin/python
import time

	
def main():
	
	import sys
	import math
	from Queue import PriorityQueue
	#from operator import itemgetter
	#from sets import Set
 
	
	#  Using metadrome 

	T= int(sys.stdin.readline().strip())
	
	for _t in range(T):
		S = sys.stdin.readline().strip()
		
		_res = S[0]
		
		for k in S[1:]:
			if ord(k) >= ord(_res[0]):
				_res = k+_res
			else:
				_res = _res+k
		
		_out = "Case #"+str(_t+1)+": "+ _res
		
		print _out
	
		
		
		
		
	
if __name__ == "__main__":
	
	#s= time.time()
	main()
	
	#print time.time()-s
	