t=int(input())
n,j=list(map(int,input().split()))
a='10000000000000011000000000000001'
print("Case #1:")
for i in range(1,501):
	td=str(format(i,"014b"))
	a=a[0]+td+a[15:17]+td+a[31]
	print(a,end=" ")
	for j in range(2,11):
		div=int(a[16:],j)
		print(div,end=" ")
	print("")