INPUT_FILE = 'A-large.in'
OUTPUT_FILE = 'A-large_out.txt'

def solve(f_in):
	word = f.readline().strip()
	final_word = word[0]
	for i in range(1,len(word)):
		if ord(word[i]) >= ord(final_word[0]):
			final_word = word[i] + final_word
		else:
			final_word = final_word + word[i]
	return final_word

with open(INPUT_FILE, 'r') as f:
	with open(OUTPUT_FILE, 'w') as f_out:
		T = int(f.readline())
		for i in range(T):
			f_out.write('Case #%d: %s\n' % (i + 1, solve(f)))
				