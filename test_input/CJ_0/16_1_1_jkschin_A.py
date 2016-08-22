import parse

def get_last_word(word):
	new_word = word[0]
	for char in word[1:]:
		prev_value = ord(new_word[0])
		cur_value = ord(char)
		if cur_value >= prev_value:
			new_word = char + new_word
		else:
			new_word = new_word + char
	return new_word

def main():
	f = open("a-large.txt", "w")
	n, l = parse.parse("A-large.in")
	n = int(n)
	for i in range(n):
		parse.write(f,i+1,get_last_word(l[i]))


main()
