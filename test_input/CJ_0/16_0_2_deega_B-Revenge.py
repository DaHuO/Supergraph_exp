#!/bin/python
def check(s):
    end = s.find('-')
    if end != -1:
        return True
    return False
def flip(s):
    temp = ''
    for i in s:
        if i == '-':
            temp += '+'
        else:
            temp += '-'
    return temp
T = int(input())
for i in range(T):
    s = input()
    c = 0
    while check(s):
        pivot = len(s)
        for j in s[::-1]:
            if j == '-':
                break
            pivot -= 1
        s = list(s)
        s[0:pivot] = flip(s[0:pivot])
        s = ''.join(s)
        c += 1
    print('Case #{}: {}'.format(i+1,c))
