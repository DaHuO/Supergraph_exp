t = int(input().strip())
for at in range(t):
    S = input().strip()
    temp = S[0]
    for i in range(1, len(S)):
        if ord(S[i]) >= ord(temp[0]):
            temp = S[i] + temp
        else:
            temp = temp + S[i]
    print('Case #{1}: {0}'.format(temp,at+1))
