import re

num_test_cases = 0
file_in = 'pancake.in'


def get_inputs(input_string):
    global num_test_cases

    test_cases = input_string.split('\n')
    num_test_cases = int(test_cases[0])

    return test_cases[1:]


def flip_pancakes(stack):
    return ''.join(['-' if cake == '+' else '+' for cake in stack[::-1]])


def evaluate_input(case_input):
    if case_input.find('-') == -1:
        return 0
    elif case_input.find('+') == -1:
        return 1
    else:
        solution = '+' * len(case_input)
        cakes = case_input
        flips = 0
        while cakes != solution:
            match = re.match(r'\++-+', cakes)
            if match:
                end = match.end()
                fix_section = cakes[:end].replace('+', '-')
                cakes = fix_section + cakes[end:]
            else:
                match = re.match(r'-+', cakes)
                end = match.end()
                fix_section = cakes[:end].replace('-', '+')
                cakes = fix_section + cakes[end:]
            flips += 1

        return flips


def main():
    with file(file_in) as fin:
        str_input = ''.join(fin.readlines()).strip()

    inputs = get_inputs(str_input)

    with file(file_in.replace('in', 'out'), 'w') as fout:
        for i in xrange(num_test_cases):
            result = evaluate_input(inputs[i])

            print 'Case #%d: %s' % (i+1, result)
            fout.write('Case #%d: %s\n' % (i+1, result))


if __name__ == '__main__':
    main()
