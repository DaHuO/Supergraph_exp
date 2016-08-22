def SOLVE(string, signal):
	if string == '+':
		if signal == 'plus':
			return 0
		else:
			return 1
	elif string == '-':
		if signal == 'plus':
			return 1
		else:
			return 0
	elif string[-1] == '+':
		if signal == 'minus':
			return 1 + SOLVE(string[:-1], 'plus')
		else:
			return SOLVE(string[:-1], 'plus')
	elif string[-1] == '-':
		if signal == 'minus':
			return SOLVE(string[:-1], 'minus')
		else:
			return 1 + SOLVE(string[:-1], 'minus')


def answer():
	source = open("B-large.in", 'r')
	output = open("large-output.txt", 'w')
	first_line = True
	case = 1
	for line in source:
		if first_line:
			first_line = False
		elif line =='\n':
			pass
		else:
			output.write("Case #{0}: {1}\n".format(case, SOLVE(line[:-1], 'plus')))
			case += 1
	source.close()
	output.close()

answer()
