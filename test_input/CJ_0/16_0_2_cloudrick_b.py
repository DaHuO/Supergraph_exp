import sys


def main():

    #f = open('B-small-attempt2.in', 'r')
    f = open('B-large.in', 'r')
    fout = open('a.out', 'w')

    case = int(f.readline())

    c = 1
    while c <= case:
        pancakes = f.readline().strip()

        def invert(s):
            i = len(s) - 1
            r = ''
            while i >= 0:
                r += '+' if s[i] == '-' else '-'
                i -= 1
            return r

        def calc(p):
            if p == '-':
                return 1
            elif p == '+' or p == '':
                return 0

            idx = len(p) - 1
            if p[idx] == '-':
                if p[0] == '-':
                    return 1 + calc(invert(p[:idx+1]))
                else:
                    idx_2 = idx - 1
                    while idx_2 >= 0:
                        if p[idx_2] == '+':
                            break
                        idx_2 -= 1
                    return 2 + calc( invert(p[idx_2+1:idx]) + p[:idx_2+1])
            return calc(p[:idx])

        fout.write('Case #%d: %d\n' % (c, calc(pancakes)))
        c += 1

if __name__ == '__main__':
    main()
