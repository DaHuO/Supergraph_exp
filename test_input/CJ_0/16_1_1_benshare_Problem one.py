f = open('A-large.in')
curr_line = f.readline()
numCases = int(curr_line)
output = open('A-large.out','w')
for case in range(1,numCases+1):	
	curr_line = f.readline()
	l = len(curr_line)
	word_so_far = curr_line[0]
	for i in range(1,l):
		word1 = word_so_far + curr_line[i]
		word2 = curr_line[i] + word_so_far
		if word1 > word2:
			word_so_far = word1
		else:
			word_so_far = word2
	
	output.write("Case #%d: %s" %(case,word_so_far))