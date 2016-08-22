def putword(string, letter):
	if string == "":
		return letter
	elif letter < string[-1]:
		return string + letter
	elif letter < string[0]:
		return string + letter
	else:
		return letter + string


def last_word(string):
	ans = ""
	for each in string:
		ans = putword(ans,each)
	return ans

if __name__ == '__main__':
		N = int(input())
		for case in range(1, N+1):
			q = input()
			a = last_word(q)
			print("Case #"+str(case)+":",a)