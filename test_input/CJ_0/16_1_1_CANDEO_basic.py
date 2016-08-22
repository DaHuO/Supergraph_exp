import sys

input_list = []
output_list = []

try:
	input_filename = sys.argv[1]
	output_filename = input_filename[:sys.argv[1].find('.')]+'.out'
except:
	print 'input filename as argv'
	exit()

def get_last_word(S):
	last_word = ''
	for w in S:
		if last_word + w > w + last_word:
			last_word = last_word + w
		else :
			last_word = w + last_word
	return last_word

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

input_list.pop(0)

for input_item in input_list:

	# do some works here
	
	result = get_last_word(input_item)
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
