#!/usr/bin/python3

T = int(input())

for t in range(1, T+1):
	pan = input()

	p = 1
	for i in range(1, len(pan)):
		if pan[i] != pan[i-1]:
			p+=1

	if pan[-1] == '+':
		p -= 1

	res = p

	print('Case #{}: {}'.format(t, res))