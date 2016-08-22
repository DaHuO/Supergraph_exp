import sys
import math



def base_power(my_string,base):
	my_sum = 0
	my_length = len(my_string)
	for xyz in xrange(0,my_length):
		my_sum = my_sum + int(my_string[xyz]) * (base**(my_length - xyz - 1))
	return my_sum

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return 2

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return divisor
    
    return True


def max_combs(my_num):
	return 2**my_num


def generateJams(jam_length,j):
	start = [0 for i in range(jam_length)]
	start[0] = 1
	start[jam_length-1] = 1
	all_jams = []
	total = 0
	for i in xrange(0,max_combs(jam_length-2)):
		curJam =  "{0:b}".format(i)
		index = 0
		if len(curJam) < jam_length-2:
			add_length = jam_length-2 - len(curJam)
			curJam = ('0' * add_length) + curJam
		for each_char in curJam:
			index = index+1
			if each_char == '0':
				start[index] = 0
			else:
				start[index] = 1
		returned_data = check_jam(start[:])
		if returned_data:
			total = total + 1
			temp_string = ''.join(str(e) for e in start[:])
			print temp_string,
			for each_num in returned_data:
				print each_num,
			print "\n",
			if total == j:
				sys.exit()

		# all_jams.append(start[:])

	# return all_jams


def check_jam(cur_jam):
	cur_jam = ''.join(str(e) for e in cur_jam)
	test_list = []
	for xyz in xrange(2,11):
		value = is_prime(base_power(cur_jam,xyz))
		if value == True:
			return False
		else:
			test_list.append(value)
	return test_list

t = int(raw_input())
for i in xrange(1, t + 1):
	n,j = [int(s) for s in raw_input().split(" ")]
	print "Case #1:"
	my_jams = generateJams(n,j)
	
	# total = 0
	# for each_jam in my_jams:
	# 	returned_data = check_jam(each_jam)
	# 	if returned_data:
	# 		total = total + 1
	# 		temp_string = ''.join(str(e) for e in each_jam)
	# 		print temp_string,
	# 		print "returned_data2: ", returned_data
	# 		if total == j:
	# 			sys.exit()


