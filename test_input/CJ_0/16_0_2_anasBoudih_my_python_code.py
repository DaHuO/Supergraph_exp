#!/usr/bin/python3
def Problem_B(N):
    for i in range(1,N+1):
        s = list(input())
        p = 0
        solu = 0
        for j in range(len(s)):
            if s[j] == '-':
                p = 1
            if s[j-1] != s[j] and j != 0:
                solu += 1
                for k in range(j):
                    if s[k] == '-':
                        s[k] = '+'
                    elif s[k] == '+' and j != len(s)-1:
                        s[k] = '-'
                p = 0
        if s[len(s)-1] == '-':
            solu += 1
	print('Case #{}: {}'.format(i,solu))
N = int(input())
Problem_B(N)

