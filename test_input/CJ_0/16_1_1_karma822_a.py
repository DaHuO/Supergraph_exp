import sys
from sys import argv

def solve(S):
	ans = ""
	for c in S:
		first = ""
		if len(ans)>0:
			first = ans[0]
		if first <= c:
			ans = c+ans
		else:
			ans = ans + c
	print(ans)

T = int(input())
for i in range(0, T):
	S = input()
	print("Case #",i+1,": ",sep="",end="")
	solve(S)
