import sys

def solve_for(case_input):
	final_minus = case_input.rfind('-')
	if final_minus == -1:
		return 0

	groups=1
	search_for='+'
	for i in range(final_minus, -1, -1):
		if case_input[i] == search_for:
			if search_for == '+':
				search_for = '-'
			else:
				search_for = '+'
			groups += 1

	return groups





lines = sys.stdin.read().split('\n')
test_cases = int(lines[0])

for i in range(1, test_cases+1):
	initial_state = lines[i]
	answer = solve_for(initial_state)
	print("Case #{0}: {1}".format(i, answer))