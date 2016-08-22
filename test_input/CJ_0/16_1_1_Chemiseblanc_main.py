#Google Codejam 2016 Round 1 Problem A
#Matthew Gibson @chemiseblanc mgibs029@uottawa.ca

import sys

input = sys.stdin.readlines()
output = open("output.txt",'w')

T = int(input[0])
print T
S = ['']*T
print S
for i in range(0,T):
	S[i] = input[i+1]
	sorted = S[i][0]
	for j in range(1,len(S[i])):
		if ord(S[i][j]) >= ord(sorted[0]):
			sorted = S[i][j] + sorted
		else:
			sorted = sorted + S[i][j]
	output.write("Case #{}: {}".format(i+1,sorted))

output.close()