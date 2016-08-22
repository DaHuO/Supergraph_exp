t=int(raw_input())
case=0
for _ in range(t):
	case+=1
	print("Case #"+str(case)+":")
	n,j=map(int,raw_input().split())
	if(n==32):
		s="10000000000000011000000000000001"
		count=0
		b=1
		while(b<501):
			ans=""
			s=s[:1]+str(format(b,'014b'))+s[15:17]+str(format(b,'014b'))+s[31:32]
			b+=1
			ans=ans+s
			for i in range(2,11):
				num=int(s[16:],i)
				ans=ans+" "+str(num)
			print(ans)
	
