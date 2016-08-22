import os
import re
import sys


def task(S):
    chars = list(S)
    result = chars[0]
    for c in chars[1:]:
        if c >= result[0]:
            result = c + result
        else:
            result += c
    return result


def main():
    with open(sys.argv[1], 'r') as f:
        src = f.read()

    lines = src.splitlines()

    T = int(lines[0])
    res = ''
    for i in range(1, T + 1):
        res += 'Case #%d: %s\n' % (i, task(lines[i]))

    with open(os.path.splitext(sys.argv[1])[0] + '.out', 'w') as f:
        f.write(res)

if __name__ == '__main__':
    main()
