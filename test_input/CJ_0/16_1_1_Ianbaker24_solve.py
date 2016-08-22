import sys

def solve(in_file, out_file, case):
	out_file.write('Case #' + str(case + 1) + ': ')
	
	word = in_file.readline().replace('\n', '')
	sorted_word = ""
	front_char = "A"
	char = ""
	i = 0
	if (len(word) > 0):
		front_char = word[0]
	while (i < len(word)):
		char = word[i]
		if (char >= front_char):
			front_char = word[i]
			sorted_word = char + sorted_word
		else:
			sorted_word = sorted_word + char
		i += 1
	
	out_file.write(sorted_word)
	out_file.write('\n')

if len(sys.argv) != 2:
	print 'Please provide one parameter with the name of the input file location relative to this file.'
else:
	in_file = open(str(sys.argv[1]), 'r')
	out_file = open(str(sys.argv[1]).replace('.in', '.out'), 'w')
	cases = int(in_file.readline())
	case = 0
	while (case < cases):
		solve(in_file, out_file, case)
		case += 1
	in_file.close()
	out_file.close()