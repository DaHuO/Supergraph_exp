inp = open("A-large.in","r")
out = open("al.out","w")

def readline(f):
    return f.readline().strip()

n = int(readline(inp))

for case in range(n):
    s = readline(inp)
    acc = ""
    for c in s:
        if acc == "":
            acc = c
        elif c >= acc[0]:
            acc = c + acc
        else:
            acc = acc + c
    out.write("Case #%d: %s\n" % (case+1,acc))

inp.close()
out.close()
