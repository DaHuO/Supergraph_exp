def last_word(s):
    w = s[0]

    for i in range(1,len(s)):
        si = ord(w[0])
        ei = ord(w[len(w)-1])

        ci = ord(s[i])

        if ci >= si:
            w = s[i] + w
        else:
            w = w + s[i]

    return w

o = open('output.txt', 'w+')
f = open('A-large.in', 'r+')
##f = open('test.txt', 'r+')
N = int(f.readline())

for i in range(N):
    s = f.readline().strip()
    
    res = last_word(s)
    print(res)

    o.write("Case #" + str(i + 1) + ": " + str(res) + "\n")

f.close()
o.close()
