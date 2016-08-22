
def solution(x):
	ans = [x[0]]
	for i in x[1:]:
		if i < ans[0]: ans.append(i)
		else: ans.insert(0, i)
	return ''.join(ans)


n = int(input())
for i in range(n):
	get = input()
	ans = solution(list(get))
	print("Case #{}: {}".format(i+1, ans))

