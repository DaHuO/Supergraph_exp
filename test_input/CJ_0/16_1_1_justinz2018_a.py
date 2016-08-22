import sys
sys.stdin = open("A-large.in", "r")
sys.stdout = open("A-l.out", "w")
n = int(input())
for i in range(n):
	s = input()
	ans = ""
	for j in s:
		ans = max(j+ans, ans+j)
	print("Case #{}:".format(i+1), ans)
