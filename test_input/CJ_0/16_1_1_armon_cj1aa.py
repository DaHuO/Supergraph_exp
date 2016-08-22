from sys import argv


def last_word(string):
    string = list(string)
    string.reverse()
    lw = []
    while len(string):
        c = string.pop()
        if len(lw) and lw[0] <= c:
            lw.insert(0, c)
        else:
            lw.append(c)

    return ''.join(lw)


if __name__=='__main__':

    fin = open(argv[1], 'r')
    tnum = int(fin.readline())
    fout = open(argv[1]+'_out', 'w')

    for i, l in enumerate(fin, 1):
        fout.write('Case #{0}: {1}'.format(i, last_word(l)))
