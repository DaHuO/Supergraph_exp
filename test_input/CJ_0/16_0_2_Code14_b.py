#! /usr/bin/env python3
'''
' Title:	Google Code Jam 2016 - B. Revenge of the Pancakes
' Author:	Cheng-Shih, Wong
' Date:		2016/04/09
'''

def sol(s):
	cnt = 0
	for i in range(slen-1):
		if s[i]!=s[i+1]: cnt += 1
	if s[-1]=='-': cnt += 1
	return cnt

T = int(input())

for ti in range(1,T+1):
	s = input()
	slen = len(s)
	print('Case #{}: {}'.format(ti, sol(s)))
