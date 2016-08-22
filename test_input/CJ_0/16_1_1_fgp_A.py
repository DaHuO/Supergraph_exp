import sys

n = int(raw_input())
nums = []

for i in range(n):
	word = raw_input()

	final_word = word[0]
	for c in word[1:]:
		if c >= final_word[0]:
			final_word = c + final_word
		else:
			final_word = final_word + c

	sys.stdout.write("Case #" + str(i+1) + ": " + final_word + "\n")
