def isFinish(cake):
	charSet = set(cake)
	if len(charSet) == 1 and '+' in charSet:
		return True
	else:
		return False

def operateCake(cake):
	start = cake[0]
	if len(cake) == 1:
		return '+'

	for index in range(1, len(cake)):
		#print str(index) + " " + str(len(cake))
		if start != cake[index]:
			if start == '+':
				return ''.join(['-' * index]) + cake[index:]
			else:
				return ''.join(['+' * index]) + cake[index:]
	if start == "-":
		return ''.join(['+' * len(cake)])

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  pancake = raw_input()
  length = len(pancake)
  tryCount = 0
  cake = pancake
  while not isFinish(cake):
  	cake = operateCake(cake)
  	tryCount = tryCount + 1
  print "Case #{}: {}".format(i, tryCount)
