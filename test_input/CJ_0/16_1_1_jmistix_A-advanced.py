import sys
sys.setrecursionlimit(9999)
input_set = "A-large.in"
#input_set = "A-small-attempt0.in"
#input_set = "A-very-small.in"
#input_set = "A-large-gen.in"

def reverse_enum(L):
   for index in reversed(xrange(len(L))):
      yield index, L[index]

def get_last_word(word):
	S = set()
	S.add(word)
	
	word_len = len(word)
	if word_len <= 1:
		return word
	max_char = max(word)

	for i, char in reverse_enum(word):
	#print i
		if char == max_char:
			left = word[:i]
			right = word[i+1:]
			
			last_left = get_last_word(left)
			last_right = right 
			return char + last_left + last_right
			#S.add(char + last_left + last_right)
	assert False
	return sorted(S, reverse=True)[0]

with open(input_set) as cases:
	case_number = 0
	next(cases)

	for data in cases:
		case_number += 1
		#print case_number
		word = data.strip()
		print "Case #{}: {}".format(case_number, get_last_word(word))