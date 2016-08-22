def main():
	f = open('A-large.in', 'r')
	t = int(f.readline())
	for i in range(t):
		s = f.readline().strip()
		print('Case #' + str(i+1) + ': ' + lastWord(s))
	f.close()
	
def lastWord(s):
	lastWord = s[0]
	s = s[1:]
	for c in s:
		if ord(c) >= ord(lastWord[0]):
			lastWord = c + lastWord
		else:
			lastWord = lastWord + c
	return lastWord

if __name__ == '__main__':
	main()
