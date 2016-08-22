#!/usr/bin/python3

from parse import get_lines

def get_lines(filename):
    lines = []
    try:
        with open(filename, 'r') as f:
            while True:
                line = f.readline().rstrip('\n')
                if line == '':
                    break
                lines.append(line)
    except EOFError:
        pass
    return lines

def solve(line):
    data = line.split(' ')
    out = data[0][0]
    for c in data[0][1:]:
        if ord(c) >= ord(out[0]):
            out = c + out
        else:
            out = out + c
    return out


if __name__ == '__main__':
    lines = (get_lines('A-large.in'))
    cases = int(lines[0])
    with open("outputA-large.txt", "w") as f:
        for case in range(0, cases):
            out = ("Case #%d: " % (case+1)) + solve(lines[case+1])
            print(out)
            f.write(out + '\n')


