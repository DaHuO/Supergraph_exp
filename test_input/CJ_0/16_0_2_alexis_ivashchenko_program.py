tests = int(input())

def replace(s):
	ret = ''
	for i in s:
		if i == '+':
			ret += '-'
		else:
			ret += '+'
	return ret

def get_result(s):
	pattern = '+' * len(s)
	
	moves = 0
	if s == pattern:
		return str(moves)
	
	index = 1
	while s != pattern:
		while index < len(s) and s[index] == s[index-1]:
			index += 1
		s = replace(s[:index]) + s[index:]
		#input()
		#print(s)
		index = 1
		moves += 1
	return str(moves)
		
	

for test in range(1, tests + 1):
	s = input()
	print('Case #%d: %s' % (test, get_result(s)))