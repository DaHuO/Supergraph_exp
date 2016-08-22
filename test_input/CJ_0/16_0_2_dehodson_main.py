input_ = open("B-large.in")
output = open("output", 'w')

cases = input_.read().split()

for i in range(0, int(cases[0])):
	case_no  = i + 1
	case     = cases[case_no]
	result   = ""

	inc = 0
	current = 0

	if(case[0:1] == '+'):
		current = 1
	else:
		current = 0
		inc = inc + 1

	for ch in case[1:]:
		if(ch == '+'):
			current = 1
		if(ch == '-'):
			if(current == 1):
				inc = inc + 2
			current = 0

	result = str(inc)

	output.write("Case #"+str(case_no)+": "+result+"\n")

output.close()