def solve(s):
    res = []
    for char in s:
        if len(res) == 0:
            res.append(char)
        else:
            if char >= res[0]:
                res.insert(0, char)
            else:
                res.append(char)
    return ''.join(res)

def main():
    T = int(raw_input())
    for i in range(1, T+1):
        S = raw_input()
        res = solve(S)
        print 'Case #%d: %s' % (i, res)

if __name__ == '__main__':
    main()
