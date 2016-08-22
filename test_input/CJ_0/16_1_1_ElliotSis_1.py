def best_word(S):
	res = S.pop(0)
	while (len(S) > 0):
		a = S.pop(0)
		if (a >= res[0]):
			res = a + res
		else:
			res = res + a

	return res

	


n_tests = int(input())

for test in range(n_tests):
	print('Case #' + str(test+1) + ': ', end='')
	S = list(input())
	print(best_word(S))