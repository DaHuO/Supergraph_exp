f = open("Alarge.in",'r')
t = int(f.readline().strip())
for i in range(t):
    s = f.readline().strip()
    word = ''
    for c in s:
        if word == '':
            word += c
        else:
            if ord(c) < ord(word[0]):
                word += c

            else:
                word = c + word

    print "Case #" + str(i+1) + ": " + word

f.close()
