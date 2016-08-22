for _ in range(int(input())):
	s=input()
	ans=s[0]
	x=s[1:]
	for i in x:
		if i<ans[0] or i<ans[len(ans)-1]:
			temp=''
			temp+=ans+i
			ans=temp
		#elif i>ans[0] or i>ans[len(ans)-1]:
		else:
			temp=''
			temp+=i+ans
			ans=temp
		'''for j in range(len(ans)):
			if s[i]>ans[j]:
				temp=ans[:j]+s[i]+ans[j:]
				ans=temp
				break
			elif s[i]<=ans[j]:
				temp=ans[:j+1]+s[i]+ans[j+1:]
				ans=temp
				break'''
	print('Case #{}: {}'.format((_+1),ans))