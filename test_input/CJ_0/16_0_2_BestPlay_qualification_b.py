import sys
import tempfile

_pancake_rev = {
    '-': '+',
    '+': '-'
}


def main():
    input_file_path = sys.argv[1]
    fd, output_file_path = tempfile.mkstemp(prefix='q_b_output.txt')
    print "output file: " + output_file_path
    with open(input_file_path) as inf, open(output_file_path, 'w') as outf:
        lines = inf.readlines()
        num_of_tests = int(lines[0].strip())

        print "num of tests: " + str(num_of_tests)

        for i in range(1, num_of_tests + 1):
            stack = list(lines[i].strip())
            num_of_flips = calc_flip_pancakes(stack)
            outf.write("Case #{0}: {1}\n".format(i, num_of_flips))


def flip_pancakes(stack, index):
    for i in range(0, index):
        stack[i] = _pancake_rev[stack[i]]


def calc_flip_pancakes(stack):
    num_of_flips = 0
    while '-' in stack:
        first_pancake = stack[0]
        idx = 0
        for j in range(1, len(stack)):
            if stack[j] != first_pancake:
                idx = j
                break
        else:
            idx = len(stack)
        flip_pancakes(stack, idx)
        num_of_flips += 1

    return num_of_flips


if __name__ == '__main__':
    main()
