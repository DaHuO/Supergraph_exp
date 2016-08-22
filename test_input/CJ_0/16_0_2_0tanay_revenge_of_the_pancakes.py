def flipPancakes(stack, number):
	return ['+' if x=='-' else '-' for x in stack[:number]][::-1] + stack[number:]

def happyPancake(stack):
	length = len(stack)
	tester = ['+'] * length

	counter = 0
	common = 1

	while stack != tester:
		
		if stack == ['-'] * length:
				stack = flipPancakes(stack, length)
				counter+=1
				return counter

		for i in range(common, length):
			if stack[i-1] != stack[i]:
				stack = flipPancakes(stack, i)
				counter+=1
				common = i
			
	return counter

out = open("rotp_large.txt", 'w')
b = 1;

for i in list(open("B-large.in", 'r'))[1:]:
	pancakes = [x for x in i if x!="\n"]
	out.write("Case #%d: %d\n" % (b, happyPancake(pancakes)))
	b+=1

out.close()