__author__ = 'igor'
T = int(input())
for i in range(T):
    S = list(input())
    s = [S[0]]
    for ch in range(1, len(S)):
        if(ord(S[ch])>=ord(s[0])):
            s = [S[ch]] + s

        else:
            s = s + [S[ch]]

    s = ''.join(s)
    print("Case #"+str(i+1)+": "+s)
