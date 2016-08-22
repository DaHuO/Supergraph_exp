'''
Google Code Jam 2016
@author: Arturo Lopez Pineda
Problem B. Revenge of the Pancakes
'''

def flip_pancakes(case, position):
	flip_case = ""
	for i in range(0, position):
		if case[i] is "-":
			flip_case = flip_case + "+"
		if case[i] is "+":
			flip_case = flip_case + "-"
	flip_case = flip_case + case[position:]
	return flip_case


def min_pancake_flips(case):
	#print "S: " + case
	min_flips = 0
	current_segment = case[0]
	for i in range(0, len(case)):
		if case[i] is not current_segment:
			case = flip_pancakes(case, i)
			#print str(i+1) + ": "+ case
			min_flips = min_flips + 1
			current_segment = case[i]
	#Flip all if negatives
	if case[0] is "-":
		case = flip_pancakes(case, len(case))
		min_flips = min_flips + 1
	#print "E: " + case
	return min_flips

# def min_pancake_flips(case):
# 	print "S: " + case
# 	min_flips = 0
# 	flip_position = 0
# 	for i in range(0, len(case)):
# 		if case[i] is "-":
# 			case = flip_pancakes(case, i+1)
# 			min_flips = min_flips + 1
# 		print str(i+1) + ": "+ case
# 	print "E: " + case
# 	return min_flips


t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
	case = str(raw_input())  # read a list of characters
	min_flips = min_pancake_flips(case)
	print("Case #{}: {}".format(i, min_flips))
	# check out .format's specification for more formatting options
