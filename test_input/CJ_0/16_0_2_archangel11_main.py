filename = "a.in"
outfilename = "output.txt"

def solve(f):
    output = 0
    arr = f.readline().strip()
    count = 0
    i = 0
    while i < len(arr) - 1:
        if arr[i] != arr[i+1]:
            count += 1
        i += 1
    if arr[-1] == '-':
        count += 1
    return count

def out(s, o):
    print s
    o.write("{}\n".format(s))

def main():
    f = open(filename)
    o = open(outfilename, 'w+')
    T = int(f.readline())
    t = 1
    while t <= T:
        output = solve(f)
        out("Case #{}: {}".format(t, output), o)
        t+=1

if __name__ == "__main__":
    main()
