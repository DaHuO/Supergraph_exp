def last_word(word):
	w = word[0]
	for l in word[1:]:
		if l < w[0]:
			w = w + l
		else:
			w = l + w
	return w

num_times = int(input())
for i in range(num_times):
	print("Case #{}: {}".format(i+1, last_word(input()).upper()))