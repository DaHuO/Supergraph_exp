def main():
	T = int(raw_input())
	for i in range(T):
		s = raw_input()
		res = ""
		first = ''
		last = ''
		for c in s:
			if c >= first:
				res = c + res
				first = c
			else:
				last = c
				res += c
		print "Case #{0}: {1}".format(i+1, res)

if __name__ == '__main__':
	main()
