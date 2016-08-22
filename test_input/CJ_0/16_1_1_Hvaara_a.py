def read(filename):
    out = []
    with open(filename) as f:
        n = int(f.readline())
        for _ in range(n):
            value = f.readline().strip()
            out.append(value)
    return out

def write(filename, out):
    with open(filename, 'w') as f:
        for i, elem in enumerate(out):
            f.write("Case #{0}: {1}\n".format(i+1, elem))

def solve(inp):
    out = ""
    for elem in inp:
        if out+elem > elem+out:
            out = out+elem
        else:
            out = elem+out
    return out

if __name__ == '__main__':
    import sys 
    filename = sys.argv[1]
    inp = read(filename)
    out = []
    for word in inp:
        out.append(solve(word))
    write(filename+'.out', out)
