with open('input', 'r') as input:
	with open('output', 'w+') as output:
		input_size = int(input.readline())
		for i in xrange(1,input_size+1):
			word = input.readline().strip()
			if not word:
				output.write("Case #%s: %s\n" % (i, word))
			else:
				result = [word[0],]
				for j in range(1,len(word)):
					if ord(result[0]) > ord(word[j]):
						result.append(word[j])
					else:
						result.insert(0, word[j]) 
				
				output.write("Case #%s: %s\n" % (i, "".join(result)))
