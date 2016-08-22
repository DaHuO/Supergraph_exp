import math

def problem1Helper2(s):

	ans = s[0]

	for i in s[1:]:
		if i >= ans[0]:
			ans = i + ans
		else:
			ans += i
	return ans



def problem1():
	data = []
	with open("CountSheepInput.txt","r") as file:
		for lines in file:
			if lines[-1] == '\n':
				lines = lines[:-1]
			data += [lines]

	for i in range(len(data[1:])):
		print "Case #" + str(i+1) + ": " +  str(problem1Helper2(data[i+1]))

problem1()