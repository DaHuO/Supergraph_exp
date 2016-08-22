def flip(arr):
	new_arr = []
	for i in arr:
		if i == '+':
			new_arr.append('-')
		else:
			new_arr.append('+')
	return new_arr

def solve(arr):
	if len(arr) == 1:
		if arr[0] == '+':
			return 0
		else :
			return 1
	else :
		b = arr[0:len(arr)-1]
		if arr[-1] == '+':	
			return solve(b)
		else :
			b = flip(b)
			return 1 + solve(b)
	


in_file = 'B-large.in'
f = open(in_file, 'r')
nb_testcase = int(f.readline().strip('\n'))

for i in range(0,nb_testcase):
	data = f.readline().strip('\n')

	data = list(data)
	ret = solve(data)
	print "Case #%d: %s"%((i+1),ret)

f.close()
