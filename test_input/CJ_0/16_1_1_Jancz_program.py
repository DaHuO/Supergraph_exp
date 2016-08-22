import sys


def read_input(in_file):
    out_file = in_file.split('.')[0] + '.out'
    with open(in_file, 'r') as i, open(out_file, 'w') as o:
        number_of_cases = int(i.readline())
        for index in range(1, number_of_cases + 1):
            line = i.readline().strip()
            result = do_algorithm(line)
            output = 'Case #{0}: {1}\n'.format(index, str(result))
            print(output)
            o.write(output)


def do_algorithm(s):
    last_word = s[0]
    for i, c in enumerate(s):
        if i == 0:
            continue
        if ord(c) >= ord(last_word[0]):
            last_word = c + last_word
        else:
            last_word = last_word + c
    return last_word


if __name__ == '__main__':
    in_file = 'example.in'
    if len(sys.argv) >= 2:
        in_file = sys.argv[1]
    read_input(in_file)
