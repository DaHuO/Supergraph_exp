import pdb

def main():
	f = open('B-large.in', 'r')
	outfile = open('results', 'w')
	case_number = 1
	for line in list(f)[1:]:
		flips = do_flips(line[0:len(line)-1])
		if (flips == 0): print('Zero   ' + line)
		outfile.write('Case #%i: %i\n' %(case_number, flips))
		case_number += 1

def do_flips(stack):
	num_flips = 0
	while '-' in stack:
		flipped = False
		i = len(stack) - 1
		while not flipped:
			if stack[0] == '+':
				first_minus = 0
				while stack[first_minus] == '+':
					first_minus += 1
				stack = flip_stack(stack, first_minus - 1)
				num_flips += 1
				flipped = True
			elif stack[i] == '-':
				stack = flip_stack(stack, i)
				num_flips += 1
				flipped = True
			i -= 1
	return num_flips

def flip_stack(stack, number):
	copy = list(stack)
	for i in range(number + 1):
		if stack[i] == '-':
			copy[number - i] = '+'
		else:
			copy[number - i] = '-'
	return copy

main()