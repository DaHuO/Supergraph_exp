fin = open("A-large.in","r")

fout = open("A-large.out","w")

T = int(fin.readline())

def solve(s):
    whiteboard = [s[0]]
    for c in s[1:]:
        if c >= whiteboard[0]:
            whiteboard = list(c)+whiteboard
        else:
            whiteboard.append(c)
    return "".join(whiteboard)

for t in range(1,T+1):
    S = fin.readline()
    res = solve(list(S))
    fout.write("Case #"+str(t)+": "+res)

fout.write("\n")
