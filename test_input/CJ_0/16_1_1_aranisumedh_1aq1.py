tc = int(input())
i=1
while tc:
	word = input()
	ans = [word[0]]
	for letter in word[1:]:
		if letter>=ans[0]:
			ans.insert(0,letter)
		else:
			ans.append(letter)
	print('Case #'+str(i)+': '+''.join(ans))
	tc-=1
	i+=1