import os

def rev(s):
	
	tmp = ""
	
	for char in s:
		if char == "+":
			tmp = "-" + tmp
		else:
			tmp = "+" + tmp
	return tmp
	
def flip(s,i):
	
	return rev(s[0:i]) + s[i:]
	
def done(s):
	
	i = 0
	for char in s[::-1]:
		if char == "+":
			i = i + 1
		else:
			break
	
	return i
	
	
def undone(s):
	
	i = 0
	for char in s[::-1]:
		if char == "+":
			i = i + 1
		else:
			break
	
	return len(s)-i
	
def undone2(s):
	
	i = undone(s)
	s = s[0:i]

	for char in s[::-1]:
		if char == "-":
			i = i - 1
		else:
			break
	
	return i
		


if __name__ == '__main__':

	file = open('IN', 'r')
	dati = file.read().split('\n')
	
	T = int(dati[0])
	
	dati = dati[1:-1]

	
	for i in range(T):
		S = dati[i]
		n = 0
		
		#print S
		
		while undone(S):
			if S[0] == "-":
				S = flip(S,undone(S))
			else:
				S = flip(S,undone2(S))
			
			#print S
			n = n + 1
			
		print "Case #%i: %i"%((i+1),n)
		
		
		
		
		
