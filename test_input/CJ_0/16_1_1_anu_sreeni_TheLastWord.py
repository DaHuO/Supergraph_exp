t=int(input())
for i in range(t):
	String=raw_input()
	result=""
	for j in String:
		if(result==""):
			result=j
		else:
			if(ord(result[0])>ord(j)):
				result=result+j
			else:
				result=j+result
	print("Case #"+str(i+1)+": "+result)
