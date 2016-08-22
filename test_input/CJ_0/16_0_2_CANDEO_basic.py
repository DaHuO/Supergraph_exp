import sys

input_list = []
output_list = []

try:
	input_filename = sys.argv[1]
	output_filename = input_filename[:sys.argv[1].find('.')]+'.out'
except:
	print 'input filename as argv'
	exit()

try:
	input_f = open("./"+input_filename)
	input_lines = input_f.readlines()
	input_count = 0
	for input_line in input_lines:
		# input_split = input_line.split()
		input_list.append(input_line.strip())
	input_f.close()
except:
	print 'read error'
	exit()

def get_E(S):
	S = S + '+'
	print S
	prev_sign = S[0]
	sign_count = 0
	for i in range(1, len(S)):
		print i, S[i]
		if S[i] == prev_sign:
			pass
		else:
			sign_count += 1
			prev_sign = S[i]
	return sign_count

input_list.pop(0)

for input_line in input_list:

	# do some works here
	
	result = get_E(input_line)
	# result += ''
	output_list.append([result])

try:
	output_f = open("./"+output_filename, "w")
	output_f.close()
except:
	pass

try:
	output_f = open("./"+output_filename, "a")
	output_str = ''

	for x in range(len(output_list)):
		output_f.write('Case #' + str(x+1)+': '+str(output_list[x][0])+"\n")
		print x
	output_f.close()
except:
	print 'write error'
	exit()
