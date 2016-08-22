def reverse_pancake(p_stack,i):
    top = p_stack[:i]
    p_stack = p_stack[i:]
    top = top[::-1]
    res = ""
    for i in top:
        if i == "-":
            res += "+"
        if i == "+":
            res += "-"
    return res+p_stack

def solve_pancake(p_stack):
    global table
    if "-" not in p_stack:
        return 0;
    queue = []
    queue.append(p_stack)
    depth = 0
    while (True):
        length = len(queue)
        for p in range(length):
            for i in range(1,len(queue[p])+1):
                a = reverse_pancake(queue[p],i)
                if (a not in table):
                    table.add(a)
                    if "-" not in a:
                        return depth+1
                    queue.append(a)
        queue = queue[length:]
        depth += 1

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)


contentsRead = readFile("B-small-attempt1.in.txt")
contentsToWrite = ""
count = 1
for c in (contentsRead.split("\n")[1:-1]):
    table = set()
    p_stack = c
    res = solve_pancake(p_stack)
    contentsToWrite += "Case #%d: " % count
    contentsToWrite += "%d" % res 
    contentsToWrite += "\n"
    count+=1

writeFile("out.txt",contentsToWrite)