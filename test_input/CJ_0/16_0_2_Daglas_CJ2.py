def main():
	cases = []
	number_of_cases = int(raw_input())
	for i in range(number_of_cases):
		cases.append(raw_input())
	
	for i,case in enumerate(cases):
		print "Case #%s: %s" % (i+1, naive_solution(case))

def flip_plus(case):
	index = 0
	new_state = ''
	while(index<len(case) and case[index] == '+'):
		new_state += '-'
		index += 1
	new_state += ''.join(case[index:])
	return new_state
	
def flip_minus(case):
	index = 0
	new_state = ''
	while(index<len(case) and case[index] == '-'):
		new_state += '+'
		index += 1
	new_state += ''.join(case[index:])
	return new_state

def naive_solution(case):
	flips = 0
	if '+' not in case:
		return 1
	if '-' not in case:
		return 0
	
	while (len(case) + 1 <> len(case.split('+'))):
		if case[0] == '+':
			case = flip_plus(case)
			flips += 1
		else:
			case = flip_minus(case)
			flips += 1
	return flips

if __name__ == "__main__":
	main()