def solve(s, i, result):
    if len(s) == i:
        return result

    tmp_result = []
    for r in result:
        tmp_result.append(s[i] + r)
        tmp_result.append(r + s[i])
    return solve(s, i + 1, tmp_result)


def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        s = raw_input()
        r = solve(s, 1, s[0:1].split())
        print 'Case #{0}: {1}'.format(i, sorted(r, reverse=True)[0])


if __name__ == '__main__':
    main()
