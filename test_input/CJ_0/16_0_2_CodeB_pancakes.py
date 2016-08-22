import fileinput
import re

def convert_basic(pancakes):
	answer = re.sub(r'([+,-])\1+', r'\1', pancakes)
	return answer

def flips(pancakes):
	l = list(pancakes)
	le = len(l)
	i = 0
	res = 0
	while i < le-1:
		if (l[i] != l[i+1]):
			res += 1
		i += 1
	if(pancakes.endswith('-')):
		res += 1
	return res


if __name__ == "__main__":
	i = 0
	for line in fileinput.input():
	    line = line.strip()
	    if i == 0:
	        testcases = int(line)
	    else:
	      pancakes = convert_basic(line)
	      if(pancakes == "+"):
	      	print ("Case #%d: 0" % i)
	      elif(pancakes == "-"):
	      	print ("Case #%d: 1" % i)
	      else:
	      	print ("Case #%d: %d" % (i, flips(pancakes)))
	    i += 1