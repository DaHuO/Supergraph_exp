def flip(s):
	t = ""
	for i in range(len(s)):
		if(s[i] == "+"):
			t += "-"
		else:
			t += "+"
	return t

def checkstring(st):
	flag = []
	f = 0
	for q in st:
		if (q == "+"):
			flag.append(True)
		else:
			flag.append(False)
		f += 1
	if(all(flag)):
		return True
	else:
		return False

def revenge(s):
	number = 0
	notflipped = True
	pancakes = s
	while(notflipped):
		# print ("pancakes", pancakes)
		if(checkstring(pancakes)):
			notflipped = False
		else:
			if (pancakes[0] == "+"):
				# print ("check", "+")
				val = "+"
			elif (pancakes[0] == "-"):
				# print ("check","-")
				val = "-"

			s = ""
			news = ""
			i = 0
			index = 0
			# for y in range(len(st)):
			while(pancakes[i] == val):
				i += 1
				if(i == len(pancakes)):
					break
			f = flip(pancakes[0:i])
			pancakes = f + pancakes[i:len(pancakes)]
			number += 1
	# print number
	return number

def main():
	f = open('B-large.in', 'r')
	fout = open('outfileBlarge.in', 'w')
	# data = f.read()
	# num = data[0]
	num = 0
	iterator = 1
	# value = 0
	line = (f.readline()).rstrip()
	# totalflips = 0
	while(line != ''):
		# print "next iteration"
		# print ("line + ", line)
		num = line
		# print num
		if (int(num) < 1 or int(num) > 100):
			print "Value of T not in range"
			break
		for i in range(0,int(num)):
			stack = (f.readline()).rstrip()
			# print "stack"
			# print stack
			# print "."
			# check = checkstring(stack)
			# print check
			noofflips = revenge(stack)
			# print (stack, noofflips)
			add = "Case #" + str(iterator)  + ": "
			final = add + str(noofflips)
			fout.write(final+'\n')
			iterator += 1
			
		line = (f.readline()).rstrip()

		
			
			# print splitnumber
		# print "All values printed"
		

	f.close()
	fout.close()

	# f1 = open('outfile.in', 'r')
	# f2 = open('outfile_final.in', 'w')
	# for line in f1:
	# 	f2.write()

if __name__ == '__main__':
	main()