def maneuver(data):
	return ['-' if x == '+' else '+' for x in data][::-1]

for test in range(1, int(raw_input()) + 1):
	answer = 0
		
	pancakes = list(raw_input())

	pivot = len(pancakes) - 1
	#print pancakes
	while True:
		#print pivot
		while pivot >= 0 and pancakes[pivot] == '+':
			pivot -= 1

		if pivot == -1:
			break
		
		if pancakes[0] == '-':
			#print pancakes[:pivot], pancakes[pivot:]
			pancakes = maneuver(pancakes[:pivot+1]) + pancakes[pivot+1:]
			answer += 1
		else:
			left = 0
			while pancakes[left] == '+':
				left += 1

			#print left, pancakes[:left] , pancakes[left:]
			pancakes = maneuver(pancakes[:left]) + pancakes[left:]
			#print pancakes
			answer += 1

		#raw_input()
	if '-' in pancakes:
		print "bah", pancakes

	print "Case #{}: {}".format(test, answer)
"""
def maneuver(data):
	return ['-' if x == '+' else '+' for x in data][::-1]

for test in range(1, int(raw_input()) + 1):
	answer = 0
		
	pancakes = list(raw_input())
	print pancakes
	pivot = len(pancakes) - 1
	left = 0
	can_flip = 0

	while pivot >= 0:
		#print pivot, pancakes[pivot], raw_input()
		if pancakes[pivot] == '+':
			if can_flip > 0:
				print "normal"
				print pivot, can_flip
				print pancakes[:pivot+1+can_flip], pancakes[pivot+1+can_flip:]
				pancakes = maneuver(pancakes[:pivot+1+can_flip]) + pancakes[pivot+1+can_flip:]
				can_flip = 0
				pivot += 1
				left = 0
				answer += 1
				print pancakes
			else:
				pivot -= 1
		else:
			if pancakes[left] == '-':
				pivot -= 1
				can_flip += 1
			else:
				#print "top"
				#print pancakes
				pancakes = maneuver(pancakes[:left+1]) + pancakes[left+1:]
				#print pancakes
				left = 0			
				answer += 1

	if can_flip > 0:
		#print "out"
		#print pancakes
		pancakes = maneuver(pancakes[:pivot+1+can_flip]) + pancakes[pivot+1+can_flip:]
		#print pancakes
		answer += 1

		if '-' in pancakes:
			print "bah", pancakes

	print "Case #{}: {}".format(test, answer)


"""

