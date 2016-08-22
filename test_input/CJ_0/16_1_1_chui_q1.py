import sys
sys.setrecursionlimit(10000)

def solving(string):
	l = len(string)
	if l <= 1:
		return string
	last = string[-1]
	ret = solving(string[:-1])
	if(ord(last) >= ord(ret[0])):
		return last + ret
	else:
		return ret + last

with open('input', 'r') as input:
	count = 0
	for line in input:
		if count == 0:
			count+=1
			continue
		print 'Case #%d: %s' % (count, solving(line.replace('\n', '')))
		count+=1