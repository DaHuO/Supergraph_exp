



if __name__ == "__main__":
	with open('A-large.in', 'r') as f:
		with open('aout.txt', 'w') as aout:
			cases = int(f.readline().rstrip())

			for i in range(cases):
				word = f.readline().rstrip()
				new_word = ""
				for letter in word:
					if not new_word:
						new_word = letter
					elif ord(new_word[0]) <= ord(letter):
						new_word = letter + new_word
					else:
						new_word = new_word + letter

				aout.write("Case #{}: {}\n".format(i+1, new_word))
