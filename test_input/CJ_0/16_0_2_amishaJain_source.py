for _ in range(int(input())):
    a=[]
    a.append(input())
    for i,s in enumerate(a):
        result=1 if s[0]=="-" else 0
        for j in range(1,len(s)):
            if s[j]=="-" and s[j-1]=="+":
                result+=2
        print("Case #",(_+1),": ",result,sep="")