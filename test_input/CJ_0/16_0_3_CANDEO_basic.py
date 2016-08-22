import sys, math

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
		input_split = input_line.split()
		for i in range(len(input_split)):
			input_split[i] = int(input_split[i])
		input_list.append(input_split)
		# input_list.append(input_line.strip())
	input_f.close()
except:
	print 'read error'
	exit()

input_list.pop(0)

def get_R(P):
	for i in range(2, int(math.sqrt(P))):
		if P % i == 0:
			return i
		else:
			pass
	return 1

for input_item in input_list:

	# do some works here
	
	# input_item[0] input_item[1]
	# 1 + 2^(input_item[0]-1) ~ 2^input_item[0] -1
	result_count = 0
	result = ''
	for i in range(1+pow(2, input_item[0]-1), pow(2, input_item[0])):
		if i % 2 == 0:
			continue
		
		str_i = bin(i)[2:]
		D_arr = [1,1,1,1,1,1,1,1,1]
		for j in range(2,11):
			int_j = int(str_i, j)
			R = get_R(int_j)
			if R == 1:
				break
			else:
				D_arr[j-2] = R
		if 1 in D_arr:
			pass
		else:
			result += '\n' + str_i + ' ' + ' '.join(map(str, D_arr))
			result_count += 1
			if result_count == input_item[1]:
				break
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
