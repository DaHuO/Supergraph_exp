def last_word(s):
    o = -1
    lw = ""
    for ch in s:
        if ord(ch) >= o:
            o = ord(ch)
            lw  = ch + lw
        else:
            lw += ch
    return lw

t = int(input())
for i in range(1, t+1):
    print("Case #"+str(i) + ": " + last_word(input()))