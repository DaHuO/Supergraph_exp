def solve(S):
    res = S[0]
    for i in S[1:]:
        if i >= res[0]:
            res = i + res
        else:
            res = res + i
    return res
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)
contentsRead = readFile("A-large.in.txt")
contentsToWrite = ""
count = 1
for c in (contentsRead.split("\n")[1:-1]):
    S = c
    res = solve(S)
    contentsToWrite += "Case #%d: " % count
    contentsToWrite +=  res 
    contentsToWrite += "\n"
    count+=1

writeFile("out.txt",contentsToWrite)