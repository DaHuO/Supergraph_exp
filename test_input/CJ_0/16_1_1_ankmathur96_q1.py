f_stub = 'A-large'
f = open(f_stub + '.in', 'r')
o = open(f_stub + '.out', 'w')
def find_last_word(ordered_alphabet):
	# print(ordered_alphabet)
	word = [ordered_alphabet[0]]
	for c in ordered_alphabet[1:]:
		if c >= word[0]:
			word.insert(0, c)
		else:
			word.append(c)
	return "".join(word)
n_cases = int(f.readline())
i = 1
while i <= n_cases:
	in_string = f.readline()
	ordered_alphabet = in_string.strip()
	word = find_last_word(ordered_alphabet)
	o.write("Case #" + str(i) + ': ' + word + '\n')
	i += 1
f.close()
o.close()