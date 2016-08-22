def get_best(s):
    res = s[0]
    for c in s[1:]:
        if c >= res[0]:
            res = c + res
        else:
            res = res + c
    return res
    

def solve():
    infile = open('A-large.in')
    outfile = open('A-large.out', 'w')
    T = int(infile.readline().strip())
    for i in range(T):
        line = 'Case #%d: %s\n' % (i+1, get_best(infile.readline().strip()))
        outfile.write(line)
    infile.close()
    outfile.close()

solve()
