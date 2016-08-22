t = eval(input())
count = 1
while t:
	s = str(input())
	output = ''
	flag = True
	for i in s:
		if flag:
			output = i
			flag = False
		else:	
			if i < output[0]:
				output += i
			else:
				output = i + output
	print("Case #",count, ": ",output, sep = "")
	count += 1
	t -= 1