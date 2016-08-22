
file_input = "A-large.in"
with open(file_input ,'r') as fd:
	lines = fd.readlines()

file_output = "A-large.out"
f = open(file_output, 'w');
	
case = 1	
for line in lines[1:]:
	lst = [line[0]]	
	for l in line[1:]:
		if lst[0] > l:
			lst = lst + [l]
		else:
			lst = [l] + lst
	# print('Case #' + str(case) + ': ' + ''.join(lst))
	f.write('Case #' + str(case) + ': ' + ''.join(lst))
	case += 1

f.close()