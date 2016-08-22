tt=int(input())+1
for t in range(1, tt):
    s=input()
    ans=""
    for c in s:
        ans=max(ans+c, c+ans)
    print("Case #{0}: ".format(t)+ans)