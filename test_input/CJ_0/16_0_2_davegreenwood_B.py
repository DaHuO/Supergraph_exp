from __future__ import division


def read(fname):
    '''
    return the input file line for line
    '''
    with open(fname, 'rb') as fid:
        data = fid.readlines()
    return data


def write(fname, case_list):
    with open(fname, 'wb') as fid:
        for i, case in enumerate(case_list):
            msg = 'Case #{}: {}\n'.format(i + 1, solve(case))
            fid.write(msg)


def parse(data):
    '''
    return a list of cases
    '''
    r, M = 1, []
    while r < len(data):
        case = data[r].strip()
        M.append(case)
        r += 1  # n
    return M


def _flop(s, k):
    return s[:k].replace('-', '*').replace('+', '-').replace('*', '+') + s[k:]


def flip(s):
    n = 0
    while '-' in s:
        hold, k = True, 0
        while k < len(s):
            if s[k] == '+' and not hold:
                break
            if s[k] == '-':
                hold = False
            k += 1
        s = _flop(s, k)
        n += 1
    return n


def f(case):
    return flip(case)


def solve(case):
    '''
    solve individual case
    return solution as string, or single scalar
    '''
    return f(case)


def main():
    infile = 'B-large.in.txt'
    outfile = 'B-out.txt'
    case_list = parse(read(infile))
    write(outfile, case_list)

if __name__ == '__main__':
    main()
