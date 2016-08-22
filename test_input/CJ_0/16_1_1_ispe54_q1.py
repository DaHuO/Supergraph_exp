#!coding=utf-8
import sys

def main():
	t = int(raw_input())
	for i in range(1, t+1):
		s = raw_input()
		print 'Case #%d: ' % i, solve(s)
		continue
	return

def solve(s):
	res = []
	for c in s:
		if len(res) == 0:
			res.append(c)
			continue
		if c < res[0]:
			res.append(c)
		else:
			res.insert(0, c)
	return ''.join(res)

if __name__ == '__main__':
	main()