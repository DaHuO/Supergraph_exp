import sys
data = sys.stdin.readlines()

t = data[0]
T = int(t)


def last_word(s):
    buf = s[0]

    for i in range(1, len(s)):

        if s[i] < buf[0]:
            # next char greater than buffer first char, append
            buf = buf + s[i]
        else:
            buf = s[i]+buf

    return buf


for i in range(1, T+1):
    string = data[i].rstrip()

    print "Case #"+str(i)+": "+last_word(string)
