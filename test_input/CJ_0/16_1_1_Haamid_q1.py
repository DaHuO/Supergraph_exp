ifile = open('A-small-attempt0.in', 'r')
T = int(ifile.readline().strip("\n"))
ofile = open('output.txt','w')

count=0
for line in ifile:
	count+=1
	ofile.write('Case #'+str(count)+': ')
	s = line.strip('\n')
	myset = set()

	for char in s:
		temp = set()
		for el in myset:
			temp.add(el)

		if len(temp)==0:
			temp.add(char)
			myset = temp
		else:
			for el in temp:
				if ord(char)>=ord(el[0]):
					myset.add(char+el)
				else:
					myset.add(el+char)

	newset = set()
	for el in myset:
		if len(el)==len(s):
			newset.add(el)
	# print newset
	for oneel in newset:
		ofile.write(oneel+'\n')

# print myset
ofile.close()
ifile.close()