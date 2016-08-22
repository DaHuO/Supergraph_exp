import itertools

def read_file():
    for line in open("A-large (1).in","r"):
        yield line.strip()

cin = read_file().next

def write_line(line):
    open("output.txt","a").write(str(line) + "\n")

cout = write_line


n = int(cin())

for _n in range(n):
    s = cin()
    ns = s[0]
    for x in s[1:]:
        if x >= ns[0]:
            ns = x + ns
        else:
            ns = ns + x

    f = 'Case #' + str(_n+1) + ': ' + ns 
    cout(f)
   
