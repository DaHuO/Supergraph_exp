#!/usr/bin/python3

T = int(input())
def compress(arr):
	if len(arr) == 0:
		return arr
	out = [arr[0]]
	for e in arr[1:]:
		if e == out[-1]:
			continue
		else:
			out.append(e)

	return out
		
for testNum in range(T):
	stack = [True if i == '+' else False for i in input()][::-1]
	# print(stack)
	compressed = compress(stack)
	# print(compressed)
	print('Case #%i: %i' %(testNum+1,len(compressed)-1 if compressed[0] else len(compressed)))

