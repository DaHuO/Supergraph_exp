def solve(word):
    char = list(word)
    myword = ""
    for c in char:
        if myword == "":
            myword += c
        else:
            if myword[0] <= c:
                myword = c + myword
            else:
                myword = myword + c

    return myword







f = open('input.txt', 'r')
o = open('output.txt', 'w')
lines = f.readlines()
T = int(lines[0])
for i in range(T):
    ans = "Case #" + str(i+1) + ": " + solve(lines[i+1].strip())
    o.write(ans + "\n")
