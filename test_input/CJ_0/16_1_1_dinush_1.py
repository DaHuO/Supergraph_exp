f = open('A-large.in', 'r')
# T = int(input())
T = int(f.readline().rstrip())
count = 1
a = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

while (T > 0):
	# S = list(input())
	S = list(f.readline().rstrip())
	out = list()
	largest = 0
	
	for l in S:
		if a[l] > largest or a[l] == largest:
			out.insert(0, l)
			largest = a[l]
		else:
			out.append(l)

	T -= 1

	print("Case #" + str(count) + ": ", end='')
	for l in out:
		print(l, end='')
	print()	
	count += 1