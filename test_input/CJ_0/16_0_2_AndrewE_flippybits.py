from itertools import groupby

#read in each stack
stacks = [line.rstrip('\n') for line in open("large")]
stacks.pop(0) #we don't need num of elements this time
#f = num of flips
f = 0
case = 1
#let's convert these - and + to bits
stacks = [s.replace('-', '0') for s in stacks]
stacks = [s.replace('+', '1') for s in stacks]
#now that we can simply add to see value
for stack in stacks:
	#I've got you right where I want you mr. pancake
	#first lets reduce the stack
	#all consecutively repeating digits can be reduced to single digits
	stack = [x[0] for x in groupby(stack)]
	stack_totality = 0
	for pancake in stack:
		stack_totality += int(pancake)
	#if the num of pancakes is equal to stack totality then we've done it
	if (len(stack) - stack_totality) != 0:
		stack = stack[::-1]
		i = 0
		while i < len(stack):
			if int(stack[i]) == 1 and i==0:
				stack.pop(i)
				f+=1
			else:
				stack[i] = 1
				f+=1
			i+=1

		print "Case #" + str(case) + ": " + str(f)
	else:
		print "Case #" + str(case) + ": " + str(f)
	case+=1
	f=0