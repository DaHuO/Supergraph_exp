def get_last(word):
	new = word[0]
	if len(word) > 1:
		for letter in word[1:]:
			if letter >= new[0]:
				new = letter + new
			else:
				new = new + letter
	return new



N = int(input())
for i in range(1,N+1):
	word = input()
	

	print("Case #{}: {}".format(i, get_last(word)))