#author : Ash-Ishh..

T = int(input())

for case in range(1,T+1):
    lis = []
    s = input()
    
    for i in s:
        if len(lis) == 0:
            lis.append(i)
        else:
            if i > lis[0]:
                lis.insert(0,i)
            elif i == lis[0]:
                lis.insert(0,i)
            else:
                lis.append(i)

    ans = ''.join(lis)
    print("Case #{0}: {1}".format(case,ans))