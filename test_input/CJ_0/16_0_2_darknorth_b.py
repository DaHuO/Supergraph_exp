def main():
	for t in range(int(input())):
		s = input()
		n = len(s)
		res = 1
		for i in range(n - 1):
			if s[i] != s[i + 1]:
				res += 1
		if s[n - 1] == '+':
			res -= 1
			
		print("Case #"+ str(t + 1) +": " + str(res))

if __name__ == '__main__':
	main()