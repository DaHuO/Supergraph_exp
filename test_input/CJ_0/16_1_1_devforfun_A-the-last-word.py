t = int(raw_input())  
for i in xrange(1, t + 1):
	word = [str(s) for s in raw_input()]  

	game_word=""

	for j, letter in enumerate(word):
  		if j==0:
			game_word=letter
		else:
			if letter>=game_word[:1]:
				game_word=letter+game_word
			else:
				game_word=game_word+letter
	
	print "Case #{}: {}".format(i, game_word)
