def run(string: str):
	result = string[0]

	for symbol in string[1:]:
		if ord(symbol) >= ord(result[0]):
			result = symbol + result
		else:
			result += symbol

	return result

if __name__ == '__main__':
	count = int(input())

	for a in range(count):
		string = input()
		result = run(string)
		print('Case #{}: {}'.format(a + 1, result))
