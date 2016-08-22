t = int(input())
for i in range(1, t + 1):
    s = list(input())
    res = s[0]
    for j in range(1, len(s)):
        if s[j] < res[0]:
            res += s[j]
        else:
            res = s[j] + res
            
    print('Case #{}: {}'.format(i, res))
    
