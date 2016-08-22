def lastword(a):
	if len(a)<2:
		return a
	ans=[a[0]]
	for i in a[1:]:
		if ord(i)>=ord(ans[0]):
			ans.insert(0,i)
		else:
			ans.append(i)
	return "".join(ans)
t=input()
f=open("out.txt","w")
for i in range(t):
	ans=lastword(raw_input())
	f.write("Case #"+str(i+1)+": "+str(ans)+"\n")
f.close()
