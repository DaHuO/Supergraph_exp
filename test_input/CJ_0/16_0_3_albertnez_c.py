N = 32
J = 500
BASES = range(2, 11)
MAXD = 1337

def find_div(n):
    for d in range(2, min(n, MAXD)):
        if (n%d) == 0:
            return d
    return None


if __name__ == "__main__":
    print("Case #1:")
    found = 0
    for i in range(1<<(N-2)):
        s = '1{0:0{1}b}1'.format(i, N-2)
        valid = True
        divs = list()
        for b in BASES:
            d = find_div(int(s,b))
            if d is None:
                valid = False
            else:
                divs.append(d)
            if not valid:
                break
        if valid:
            print('{0} {1}'.format(s, ' '.join(map(str,divs))))
            found += 1
        if found == J:
            break

