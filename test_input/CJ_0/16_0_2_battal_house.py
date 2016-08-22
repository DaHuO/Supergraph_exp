import sys

def compress(seq):
    last_elt = None
    new_seq = []

    for s in seq:
        if not s == last_elt:
            new_seq.append(s)
            last_elt = s

    return new_seq

def least_flips(seq):
    new_seq = compress(seq)

    if new_seq[-1] == '+':
        return len(new_seq) - 1
    else:
        return len(new_seq)

def print_case(case_number, res):
    print("Case #%d: %s" % (case_number, str(res)))

def parse_limits(line):
    return int(line.strip())

def parse_test(line):
    return list(line.strip())

def run():
    # Parse input
    lines = sys.stdin.read().split('\n')
    T = parse_limits(lines[0])
    lines = lines[1:]

    # Run program and get output
    for i in range(0, T):
        seq = parse_test(lines[i])
        print_case(i + 1, least_flips(seq))

if __name__ == '__main__':
    run()
