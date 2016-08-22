def the_last_word(s):
	
	w = [s[0]]

	for i in xrange(1, len(s)):
		if s[i] < w[0]:
			w.append(s[i])
		else:
			w.insert(0, s[i])

	return ''.join(w)



def main():

	t = int(input())

	for i in xrange(1, t + 1):
		s = raw_input()

		print("Case #{}: {}".format(i, the_last_word(s)))




main()
