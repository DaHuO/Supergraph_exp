import sys


def main():

    #f = open('A-small-attempt0.in', 'r')
    f = open('A-large.in', 'r')
    fout = open('a.out', 'w')

    case_all = int(f.readline())

    case = 1
    while case <= case_all:
        s = f.readline().strip()
        out = ''

        for c in s:
            if not out or c >= out[0]:
                out = c + out
            else:
                out = out + c

        fout.write('Case #%d: %s\n' % (case, out))
        case += 1

    f.close()
    fout.close()

if __name__ == '__main__':
    main()
