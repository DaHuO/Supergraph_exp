class PancakeSorter(object):
	def __init__(self, pancake_list):
		self.pancake_list = pancake_list
		self.iterations = 0

	def make_positive(self, right_index):
		count = 0
		while(right_index > -1 and self.pancake_list[right_index] == '+'):
			right_index -= 1
		while(right_index>-1):
			if self.pancake_list[right_index] == '-':
				count = 1
				right_index -= 1
			else:
				# This is to optimize for tail recursion
				return (self.make_negative, right_index)
				
		return count
	
	def make_negative(self, right_index):
		count = 0
		while(right_index > -1 and self.pancake_list[right_index] == '-'):
			right_index -= 1
		while(right_index>-1):
			if self.pancake_list[right_index] == '+':
				count = 1
				right_index -= 1
			else:
				# This is to optimize for tail recursion
				return (self.make_positive, right_index)
				
		return count

	def count_iterations(self):
		result = self.make_positive(len(self.pancake_list)-1)
		while(type(result) is tuple):
			self.iterations += 1
			result = result[0](result[1])
		self.iterations += result
		return self.iterations
	

with open('input', 'r') as input:
	with open('output', 'w+') as output:
		input_size = int(input.readline())
		for i in xrange(1,input_size+1):
			pancake_list = list(input.readline().strip())
			sorter = PancakeSorter(pancake_list)
			output.write("Case #%s: %s\n" % (i, sorter.count_iterations()))
