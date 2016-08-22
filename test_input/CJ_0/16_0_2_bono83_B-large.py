
def total_flipping_count(stack):
	flip_count = 0
	cal_stack = stack
	while(True):
		if all_happy_side(cal_stack):
			return flip_count
		else:
			cal_stack = flip_pancakes(cal_stack)	
		flip_count += 1


def all_happy_side(stack):
	for c in stack:
		if c is "-":
			return False
	return True


def flip_pancakes(stack):
	part_stack = []
	pos = 0
	for cake in stack:
		if pos > 0 and part_stack[pos-1] is not cake:
			return flipping(stack, part_stack)
		else:
			part_stack.append(cake)
		pos += 1	

	return flipping(stack, part_stack)
	

def flipping(stack, part_stack):
	temp_stack = []
	for c in part_stack:
		temp_stack.append("-" if c is "+" else "+")
	temp_stack.reverse()	
	return temp_stack + stack[len(temp_stack):len(stack)]


t = int(input())
for i in range(1, t + 1):
	pancake_stack = [c for c in input()]
	print("Case #{}: {}".format(i, total_flipping_count(pancake_stack)))
