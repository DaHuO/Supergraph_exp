def encodeStr(s):
	answer = []
	for ch in s:
		if ch=='+':
			answer.append(1)
		else:
			answer.append(-1)
	return answer

def stripOnes(arr):
	index = len(arr)-1
	while index>=0:
		if arr[index] == 1:
			index = index-1
		else:
			break
	return index+1

def stripNegs(arr):
	index = len(arr)-1
	while index>=0:
		if arr[index] == -1:
			index = index-1
		else:
			break
	return index+1


f = open('B-large.in')
count = int(f.readline())
for i in range(1,count+1):
	string = f.readline().rstrip()
	array = encodeStr(string)
	#print (string, array)
	passes = 0
	length = len(array)
	while length !=0:
		#print 'Before striping'
		#print array
		index1 = stripOnes(array)
		array = array[:index1]
		#print 'After striping ones'
		#print array
		index2 = stripNegs(array)
		array = array[:index2]
		#print 'After striping NEG ones'
		#print array
		if index2 < index1:
			passes = passes+1
			array[:] = [x*(-1) for x in array]
		length = len(array)
	print ('CASE #'+str(i)+': '+str(passes))

			
f.close()

