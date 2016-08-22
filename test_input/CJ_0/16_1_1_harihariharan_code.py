def compute_last_word(input_chars):
    seen_so_far = ""
    for current_char in input_chars:
        if len(seen_so_far) == 0:
            seen_so_far += current_char
        else:
            if current_char >= seen_so_far[0]:
                seen_so_far = current_char + seen_so_far
            else:
                seen_so_far = seen_so_far + current_char
    return seen_so_far


if __name__ == "__main__":
	N = input()
	result = []
	for i in xrange(N):
		input_chars = raw_input()
		result.append(compute_last_word(input_chars))

	for i in xrange(N):
		print "Case #"+str(i+1)+": "+result[i]
