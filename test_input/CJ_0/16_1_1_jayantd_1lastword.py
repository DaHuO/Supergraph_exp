#!/usr/bin/env python


def find_max(S):
	if len(S) == 0:
		return ''

	max_char = sorted(S, reverse=True)[0]
	#print "max_char = ", max_char
	L = []
	n_max = 0
	for i, s in enumerate(S):
		if s == max_char: # this is a max letter
			L.append(None)
			n_max += 1
		else:
			L += s

	S_rem = max_char * n_max
	for i, l in enumerate(L):
		if l == None:
			break

	S_sub_left = ''.join([x for x in L[0:i] if x != None])
	S_sub_right = ''.join([x for x in L[i:] if x != None])
	S_rem += find_max(S_sub_left) + S_sub_right

	return S_rem


def main():

	filename = "A-large.in"
	f = open(filename, 'r')
	o = open(filename + "_out", 'w')

	T = int(f.readline())

	for t in range(T):
		S = f.readline()
		o.write("Case #" + str(t + 1) + ": ")

		S = S.split("\n")[0]
		o.write(find_max(S) + "\n")


if __name__ == "__main__":
	main()
