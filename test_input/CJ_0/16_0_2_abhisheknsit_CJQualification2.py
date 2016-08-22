ifile = 'B-large.in'
ofile = 'output.txt'
input = open(ifile, 'r')
output = open(ofile, 'w')
flipflop = ['-', '+']
def count_flips(inp):
    count = 0
    flip = 1

    inp = inp.strip()
    if inp[0]=='-' and len(inp)==1:
        return 1
    if inp[0]!=flipflop[flip]:
        flip^=1
    for c in inp:
        if c == flipflop[flip]:
            count += 1
            flip ^= 1
    if inp[-1] == '+':
        count-=1
    return count


i = int(input.readline())
for j in xrange(1, i+1):
    inp = input.readline()
    ans = count_flips(inp)
    st = 'Case #%d: %d\n' % (j, ans)
    output.write(st)