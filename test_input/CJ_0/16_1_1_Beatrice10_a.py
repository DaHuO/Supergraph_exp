# 160415 by beatrice
import sys
import re
	
input = raw_input()
T = int(input)
result = []
for l in range(0, T):
	oldstr = raw_input()
	newstr = []
	max = 'A'
	last = oldstr[0]

	le = len(oldstr)
	#for i in range(0, le):
	#	if oldstr[i] > max:
	#		max = oldstr[i]
	#print(max)

	newstr.append(last)
	for i in range(1, le):
		if oldstr[i] > max:
			max = oldstr[i]
			
		if oldstr[i] > newstr[0]:
			newstr.insert(0, oldstr[i])
		elif oldstr[i] == newstr[0] and oldstr[i] == max:
			newstr.insert(0, oldstr[i])
		else:
			newstr.append(oldstr[i])
		last = oldstr[i]

	result.append([])
	result[l].extend(newstr)
	
for i in range(0, T):
	s = ''
	s += 'Case #'
	s += str(i+1)
	s += ': '
	le = len(result[i])
	for j in range(0, le):
		s += result[i][j]
	print(s)
	#print("")