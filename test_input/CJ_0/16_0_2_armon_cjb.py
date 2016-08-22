from sys import argv

def get_happy(pc):
    flips = 0
    seen = False
    p = '+'
    for c in pc:
        if c == '-':
            flips += (p!='-')
            flips += seen
            seen = False
        else:
            seen = True
        p = c
    return flips

if __name__=='__main__':

    fin = open(argv[1], 'r')
    tnum = int(fin.readline())
    fout = open(argv[1]+'_out', 'w')

    for i, l in enumerate(fin, 1):
        fout.write('Case #{0}: {1}\n'.format(i, get_happy(l.strip())))
