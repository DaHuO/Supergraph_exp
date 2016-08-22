A = int(raw_input())
for i in range(A):
	input1 = list(raw_input())
	output = []
	output.append(input1[0])
	for j in range(1,len(input1)):
		if ord(input1[j]) == ord(output[0]):
			output.insert(0, input1[j])		
		elif ord(input1[j]) == ord(output[len(output)-1]):
			output.insert(len(output), input1[j])		
		elif ord(input1[j]) < ord(output[0]):
			output.append(input1[j])
		elif ord(input1[j]) > ord(output[0]):
			output.insert(0, input1[j])


	print "Case #" + str(i+1)+": "+ "".join(output)
